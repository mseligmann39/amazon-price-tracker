@echo off
set PROFILE_PATH=C:\whatsapp_profile
echo.
echo ✅ Abriendo Chrome con perfil exclusivo para WhatsApp Web...
echo.
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir=%PROFILE_PATH% --profile-directory=Default https://web.whatsapp.com
echo.
echo 🔄 Espera a que cargue WhatsApp Web y escanea el código QR si es necesario.
echo.
pause
