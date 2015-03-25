@echo off
for /f "tokens=2 delims= " %%I IN ('svn st --no-ignore ^| findstr /R "^[I?]"') DO (
    rem проверка каталог или файл
    for %%d IN (%%I) DO (
        IF EXIST %%~sd\NUL (
            rmdir /S /Q "%%I"
        ) ELSE (
            del /F /Q %%I
        )
    )
)
