# ফাইলের একদম শেষে (main() এর পর) যোগ করুন
import os
PORT = int(os.environ.get('PORT', 8000))

# M3U ফাইল সার্ভ করার জন্য একটি সিম্পল সার্ভার
from http.server import HTTPServer, SimpleHTTPRequestHandler
os.chdir('/opt/render/project/src')  # রেন্ডারের ওয়ার্কিং ডিরেক্টরি
httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
print(f"Serving M3U file at port {PORT}")
httpd.serve_forever()
