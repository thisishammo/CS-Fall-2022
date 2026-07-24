#!/usr/bin/env python3
"""
Project 01 Submission Server
Generates and hosts project_01.zip for download
"""

import os
import sys
import http.server
import socketserver
from pathlib import Path
import zipfile
import shutil
from urllib.parse import unquote

# Configuration
PORT = 8000
SCRIPT_DIR = Path(__file__).parent.resolve()

class ProjectSubmissionHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP handler for project submission"""
    
    def do_GET(self):
        """Handle GET requests"""
        try:
            if self.path == '/' or self.path == '/index.html':
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                html_content = self.get_index_html().encode('utf-8')
                self.send_header('Content-Length', len(html_content))
                self.end_headers()
                self.wfile.write(html_content)
            elif self.path == '/download':
                self.download_zip()
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>404 - Not Found</h1>')
        except Exception as e:
            print(f"Error handling request: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>500 - Internal Server Error</h1>')
    
    def do_HEAD(self):
        """Handle HEAD requests"""
        try:
            if self.path == '/download':
                zip_path = SCRIPT_DIR / 'project_01.zip'
                if zip_path.exists():
                    file_size = zip_path.stat().st_size
                    self.send_response(200)
                    self.send_header('Content-type', 'application/zip')
                    self.send_header('Content-Disposition', 'attachment; filename="project_01.zip"')
                    self.send_header('Content-Length', file_size)
                    self.end_headers()
                else:
                    self.send_response(404)
                    self.end_headers()
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
        except Exception as e:
            print(f"Error handling HEAD request: {e}")
            self.send_response(500)
            self.end_headers()
    
    def download_zip(self):
        """Serve the project_01.zip file for download"""
        zip_path = SCRIPT_DIR / 'project_01.zip'
        
        if not zip_path.exists():
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Error: project_01.zip not found</h1>')
            return
        
        try:
            file_size = zip_path.stat().st_size
            
            # Set headers for file download
            self.send_response(200)
            self.send_header('Content-type', 'application/zip')
            self.send_header('Content-Disposition', 'attachment; filename="project_01.zip"')
            self.send_header('Content-Length', file_size)
            self.end_headers()
            
            # Send file in chunks
            chunk_size = 8192
            with open(zip_path, 'rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
        except Exception as e:
            print(f"Error downloading file: {e}")
            self.send_response(500)
            self.end_headers()
    
    def get_index_html(self):
        """Return the HTML page with download link"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project 01 Submission</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            max-width: 600px;
            width: 100%;
            padding: 40px;
            text-align: center;
        }
        
        .header {
            margin-bottom: 30px;
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 32px;
        }
        
        .subtitle {
            color: #666;
            font-size: 16px;
            margin-bottom: 20px;
        }
        
        .deliverables {
            background: #f5f5f5;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 30px 0;
            border-radius: 5px;
            text-align: left;
        }
        
        .deliverables h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 18px;
        }
        
        .deliverables ul {
            list-style: none;
        }
        
        .deliverables li {
            color: #555;
            padding: 8px 0;
            font-size: 14px;
            border-bottom: 1px solid #ddd;
        }
        
        .deliverables li:last-child {
            border-bottom: none;
        }
        
        .deliverables li:before {
            content: "✓ ";
            color: #667eea;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .points {
            color: #666;
            font-size: 13px;
            margin-left: 20px;
        }
        
        .download-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin: 30px 0;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
        }
        
        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        
        .download-btn:active {
            transform: translateY(0);
        }
        
        .info-box {
            background: #e3f2fd;
            border: 1px solid #90caf9;
            color: #1565c0;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            font-size: 14px;
        }
        
        .footer {
            color: #999;
            font-size: 12px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }
        
        .status {
            display: inline-block;
            background: #4caf50;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            margin-bottom: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="status">✓ Ready for Submission</div>
            <h1>Project 01 Submission</h1>
            <p class="subtitle">CS Fall 2022 - Assignment Package</p>
        </div>
        
        <div class="deliverables">
            <h3>📦 Deliverables (6 Files)</h3>
            <ul>
                <li>p1_slices.py<span class="points">(17 points)</span></li>
                <li>p1_steps.py<span class="points">(17 points)</span></li>
                <li>p1_walk.py<span class="points">(17 points)</span></li>
                <li>p1_pythagorean.py<span class="points">(17 points)</span></li>
                <li>p1_cement.py<span class="points">(17 points)</span></li>
                <li>p1_travel.py<span class="points">(17 points)</span></li>
            </ul>
        </div>
        
        <div style="color: #666; font-size: 16px; font-weight: bold;">
            Total: 102 Points + 2 Extra Credit
        </div>
        
        <a href="/download" class="download-btn" download="project_01.zip">
            📥 Download project_01.zip
        </a>
        
        <div class="info-box">
            <strong>ℹ️ Instructions:</strong><br>
            1. Click the download button to get project_01.zip<br>
            2. Upload the zip file to Canvas<br>
            3. Verify submission before deadline<br>
            ⚠️ Note: Filenames are CASE-SENSITIVE
        </div>
        
        <div class="footer">
            <p>Generated automatically from Project 1 Python files</p>
            <p>Server running on port 8000 • Ready for local submission</p>
        </div>
    </div>
</body>
</html>
"""
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def generate_zip():
    """Generate project_01.zip from all Python files"""
    zip_path = SCRIPT_DIR / 'project_01.zip'
    temp_dir = SCRIPT_DIR / 'project_01_temp'
    
    print("📦 Generating project_01.zip...")
    
    try:
        # Create temporary directory
        temp_dir.mkdir(exist_ok=True)
        
        # Files to include
        files_to_copy = [
            ("Project 1/Assignment 1/p1_slices.py", "p1_slices.py"),
            ("Project 1/Assignment 2/p1_steps.py", "p1_steps.py"),
            ("Project 1/Assignment 3/p1_walk.py", "p1_walk.py"),
            ("Project 1/Assignment 4/p1_pythagorean.py", "p1_pythagorean.py"),
            ("Project 1/Assignment 5/p1_cement.py", "p1_cement.py"),
            ("Project 1/Assignment 6/p1_travel.py", "p1_travel.py"),
        ]
        
        # Copy files
        for src_path, dest_name in files_to_copy:
            src = SCRIPT_DIR / src_path
            if not src.exists():
                print(f"  ⚠️  Warning: {src_path} not found")
                continue
            
            dst = temp_dir / dest_name
            shutil.copy2(src, dst)
            print(f"  ✓ Copied {dest_name}")
        
        # Create zip file
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in temp_dir.glob('*.py'):
                zipf.write(file, arcname=file.name)
        
        # Cleanup
        shutil.rmtree(temp_dir)
        
        print(f"✓ Zip file created: {zip_path}")
        print(f"  Size: {zip_path.stat().st_size:,} bytes")
        
        return True
        
    except Exception as e:
        print(f"✗ Error generating zip: {e}")
        return False


def main():
    """Main server function"""
    # Generate zip file first
    if not generate_zip():
        sys.exit(1)
    
    # Start server
    try:
        handler = ProjectSubmissionHandler
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print(f"\n🚀 Server started successfully!")
            print(f"📍 Access at: http://localhost:{PORT}")
            print(f"📍 Or: http://127.0.0.1:{PORT}")
            print(f"\nPress Ctrl+C to stop the server\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")
    except OSError as e:
        print(f"\n✗ Error: Could not start server on port {PORT}")
        print(f"  {e}")
        print(f"\n  Try using a different port:")
        print(f"    python3 submit_server.py 9000")
        sys.exit(1)


if __name__ == '__main__':
    # Allow custom port as argument
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            sys.exit(1)
    
    main()
