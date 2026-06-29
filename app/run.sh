#!/usr/bin/env bash
# Launch the WAI-Research Agent Operations Dashboard (Streamlit app) on your Mac.
# Usage:  ./run.sh        (from the app/ folder)
set -e
cd "$(dirname "$0")"

# Install deps the first time if streamlit isn't available.
if ! python3 -c "import streamlit" 2>/dev/null; then
  echo "Installing dashboard dependencies (first run only)..."
  python3 -m pip install --user -r requirements.txt
fi

PORT="${PORT:-8501}"
URL="http://localhost:${PORT}"
echo "Starting the WAI-Research dashboard at ${URL}"
# Open the Mac browser shortly after the server starts.
( sleep 2; open "${URL}" >/dev/null 2>&1 || true ) &
exec python3 -m streamlit run dashboard.py --server.port "${PORT}"
