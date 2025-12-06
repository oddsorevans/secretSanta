#!/bin/bash

echo "🎅 Starting Secret Santa Web Application..."
echo ""

# Check if virtual environment exists for backend
if [ ! -d "backend/venv" ]; then
    echo "Creating Python virtual environment..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd ..
else
    echo "✓ Python virtual environment found"
fi

# Check if node_modules exists for frontend
if [ ! -d "frontend/node_modules" ]; then
    echo "Installing frontend dependencies..."
    cd frontend
    npm install
    cd ..
else
    echo "✓ Frontend dependencies found"
fi

echo ""
echo "Starting services..."
echo ""

# Start backend
echo "Starting Flask backend on http://localhost:5001..."
echo "(Note: Using port 5001 to avoid macOS AirPlay conflict on port 5000)"
cd backend
source venv/bin/activate
python app.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 2

# Start frontend
echo "Starting Vue frontend on http://localhost:5173..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✓ Services started!"
echo ""
echo "🎄 Open your browser to: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both services"
echo ""

# Wait for Ctrl+C
trap "echo ''; echo 'Stopping services...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
