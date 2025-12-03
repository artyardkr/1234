import re
import os

source_file = '/Users/songhyowon/Downloads/소행론ppt/all_slides_view.html'
target_file = '/Users/songhyowon/Downloads/소행론ppt/presentation_slides.html'

print(f"Reading from {source_file}...")
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head content
print("Extracting head content...")
head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
if head_match:
    head_inner = head_match.group(1)
    # Update title
    head_inner = re.sub(r'<title>.*?</title>', '<title>Presentation Mode</title>', head_inner)
else:
    print("Warning: No head tag found.")
    head_inner = ""

# Extract slides
print("Extracting slides...")
lines = content.splitlines()
slides = []
current_slide_lines = []
in_slide = False

for line in lines:
    if '<div class="slide-container">' in line:
        in_slide = True
        # Add the wrapper class for JS selection
        current_slide_lines = ['        <div class="slide-container slide-wrapper">']
        continue
    
    if in_slide:
        # Check for closing div of the container.
        # Based on the file structure, it is "    </div>" (4 spaces).
        if line == '    </div>':
            current_slide_lines.append(line)
            slides.append('\n'.join(current_slide_lines))
            in_slide = False
        else:
            current_slide_lines.append(line)

print(f"Found {len(slides)} slides.")

# New HTML Content
new_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
{head_inner}
    <style>
        /* Overrides and New Styles */
        body {{
            margin: 0;
            padding: 0;
            background-color: #1a1a1a; /* Dark background */
            overflow: hidden; /* No scrolling */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Noto Sans KR', sans-serif;
        }}
        
        /* Container for scaling */
        #slideshow-container {{
            width: 1280px;
            height: 720px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            transform-origin: center center;
            box-shadow: 0 0 50px rgba(0,0,0,0.5);
        }}

        .slide-container {{
            margin: 0 !important; /* Override original margin */
            position: absolute; /* Stack them */
            top: 0;
            left: 0;
            /* Ensure it takes full space of the container */
            width: 100%; 
            height: 100%;
        }}

        .slide-wrapper {{
            display: none;
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
        }}
        
        .slide-wrapper.active {{
            display: block;
            opacity: 1;
        }}

        /* Controls */
        #controls {{
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 12px 30px;
            border-radius: 50px;
            display: flex;
            gap: 24px;
            align-items: center;
            z-index: 1000;
            color: white;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        
        .control-btn {{
            background: none;
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            padding: 5px;
            transition: all 0.2s;
            opacity: 0.8;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .control-btn:hover {{
            opacity: 1;
            transform: scale(1.1);
            color: #0b6e69; /* brand-main */
        }}
        
        .control-btn:disabled {{
            opacity: 0.3;
            cursor: not-allowed;
            transform: none;
        }}
        
        #slide-counter {{
            font-weight: 500;
            min-width: 80px;
            text-align: center;
            font-variant-numeric: tabular-nums;
            letter-spacing: 1px;
        }}

        /* Fullscreen button */
        #fullscreen-btn {{
            margin-left: 10px;
            border-left: 1px solid rgba(255,255,255,0.3);
            padding-left: 20px;
        }}
    </style>
</head>
<body>

    <div id="slideshow-container">
        {''.join(slides)}
    </div>

    <div id="controls">
        <button id="prev-btn" class="control-btn" title="Previous (Left Arrow)"><i class="fas fa-chevron-left"></i></button>
        <span id="slide-counter">1 / {len(slides)}</span>
        <button id="next-btn" class="control-btn" title="Next (Right Arrow / Space)"><i class="fas fa-chevron-right"></i></button>
        
        <button id="fullscreen-btn" class="control-btn" title="Toggle Fullscreen (F)">
            <i class="fas fa-expand"></i>
        </button>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide-wrapper');
        const totalSlides = slides.length;
        let currentSlide = 0;
        const counter = document.getElementById('slide-counter');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const fullscreenBtn = document.getElementById('fullscreen-btn');
        const container = document.getElementById('slideshow-container');

        function showSlide(index) {{
            if (index < 0) index = 0;
            if (index >= totalSlides) index = totalSlides - 1;
            
            slides.forEach((slide, i) => {{
                if (i === index) {{
                    slide.classList.add('active');
                }} else {{
                    slide.classList.remove('active');
                }}
            }});
            
            currentSlide = index;
            counter.textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
            
            prevBtn.disabled = currentSlide === 0;
            nextBtn.disabled = currentSlide === totalSlides - 1;
        }}

        function resizeSlides() {{
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;
            const slideWidth = 1280;
            const slideHeight = 720;
            
            const scaleX = windowWidth / slideWidth;
            const scaleY = windowHeight / slideHeight;
            const scale = Math.min(scaleX, scaleY) * 0.95; // 95% to leave some margin
            
            container.style.transform = `scale(${{scale}})`;
        }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(err => {{
                    console.log(`Error attempting to enable fullscreen: ${{err.message}}`);
                }});
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }}

        window.addEventListener('resize', resizeSlides);
        resizeSlides(); // Initial call

        prevBtn.addEventListener('click', () => showSlide(currentSlide - 1));
        nextBtn.addEventListener('click', () => showSlide(currentSlide + 1));
        fullscreenBtn.addEventListener('click', toggleFullscreen);

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowLeft') showSlide(currentSlide - 1);
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') showSlide(currentSlide + 1);
            if (e.key === 'f' || e.key === 'F') toggleFullscreen();
        }});

        // Initialize
        showSlide(0);
    </script>
</body>
</html>
"""

print(f"Writing to {target_file}...")
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done!")
