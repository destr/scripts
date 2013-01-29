#!/bin/bash

xmodel_root_dir=
build_deb_pack="src/scripts/build-deb-pack.sh"
debian_subdir="debian"
pkgs_subdir="pkgs"

version=
revision=
no_remove=false


# список проектов и порядок их сборки
projects=( tbx xrti world xtss )

function remove_packages() {
# удаляем пакеты, которые собираются.
# если название пакета будет содержать точки, то он не будет удалён
# $1 - название проекта
    debian_dir="$xmodel_root_dir"/"$1"/"$debian_subdir"
    pushd "$debian_dir"
    dpkg -P `ls -1 *.install | cut -d . -f 1`
    popd
}

function build_tbx() {
    local tbx_dir="$xmodel_root_dir/tbx"
    "$tbx_dir"/"$build_deb_pack" -a amd64 -r $revision -v $version -p tbx -s "$tbx_dir"

    if [[ $? -ne 0 ]];then
        exit 3
    fi
    # установка собранных пакетов
    dpkg -i "$tbx_dir"/"$pkgs_subdir"/*.deb
}

function build_xrti() {
    local xrti_dir="$xmodel_root_dir/xrti"
    "$xrti_dir/$build_deb_pack" -a amd64 -r $revision -v $version -p xrti -s "$xrti_dir"
    if [[ $? -ne 0 ]];then
        exit 3
    fi
    dpkg -i "$xrti_dir/$pkgs_subdir"/*.deb
}

function build_world() {
    local world_dir="$xmodel_root_dir/world"
    # собираем fakefom
    # надо ещё удалять
    pushd "$world_dir/src/basefom/_fomxml"
    dpkg-buildpackage -us -uc
    dpkg -i ../*.deb
    popd

    "$world_dir/$build_deb_pack" -a amd64 -r $revision -v $version -p world -s "$world_dir"
    if [[ $? -ne 0 ]];then
        exit 3
    fi
    dpkg -i "$world_dir/$pkgs_subdir"/*.deb
}

function build_xtss() {
    local xtss_dir="$xmodel_root_dir/xtss"
    "$xtss_dir/$build_deb_pack" -a amd64 -r $revision -v $version -p xtss -s "$xtss_dir"

    if [[ $? -ne 0 ]];then
        exit 3
    fi
    dpkg -i "$xtss_dir/$pkgs_subdir"/*.deb
}

function usage() {
    echo "usage `basename $0`"
    echo "-h — show this help"
    echo "-x — xmodel root dir"
    echo "-V — project version"
    echo "-R — project revision"
    echo "-p — build only this project"
    echo "-n — no remove installed packages"
}

if [[ "$(id -u)" != "0" ]];then
    echo "Only root may run this script"
    exit 2
fi

declare -a user_projects
while getopts x:V:p:R:hn opt
do
    case "$opt" in
        x) xmodel_root_dir=`readlink -e "$OPTARG"`;;
        h) usage ;;
        V) version=$OPTARG;;
        R) revision=$OPTARG;;
        p) user_projects+=( $OPTARG );;
        n) no_remove=true
    esac
done

if [[ -z "$xmodel_root_dir" ]]; then
    echo "xmodel_root_dir not set or not exist"
    exit 1
fi

build_projects=${projects[@]}

if [[ ${#user_projects[@]} != 0  ]];then
    build_projects=${user_projects[@]}
fi

if ! $no_remove; then
    # удаляем все пакеты который собираются и устанавливаются в рамках проекта
    for ((i=${#build_projects[@]}-1; i>=0; i--))
    do
        project=${build_projects[$i]}
        echo Remove all packages from $project
        remove_packages $project
    done
fi

for project in ${build_projects[@]}
do
    run="build_$project"
    eval $run
done

