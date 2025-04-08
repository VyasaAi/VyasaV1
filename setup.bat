@echo off
echo Setting up VyasaAi project...

:: Step 1: Create virtual environment
python -m venv venv

:: Step 2: Activate virtual environment
call venv\Scripts\activate

:: Step 3: Upgrade pip
python -m pip install --upgrade pip

:: Step 4: Install dependencies
pip install -r requirements.txt

:: Step 5: Create folders if they don't exist
mkdir app
mkdir app\models
mkdir app\routes
mkdir app\services

:: Step 6: Create placeholder files if not already present
echo. > app\main.py
echo. > app\db.py
echo. > app\models\order.py
echo. > app\routes\order_routes.py
echo. > app\services\oracle_erp.py
echo. > .env

echo Setup complete! ✅
pause
