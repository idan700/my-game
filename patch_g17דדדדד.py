# -*- coding: utf-8 -*-
import re

filepath = '/sessions/bold-confident-feynman/mnt/outputs/כובש_השטחים.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

orig_len = len(content)
print(f"Original length: {orig_len}")

# ─────────────────────────────────────────────────────────────────
# 1.  CSS
# ─────────────────────────────────────────────────────────────────
CSS_ANCHOR = '.gc-16:hover{box-shadow:0 8px 32px rgba(0,255,140,0.5);}'
CSS_NEW = r"""
/* ── Game 17 – הנסיכה הקסומה ── */
.gc-17{background:linear-gradient(145deg,#130025,#3d006b);box-shadow:0 4px 22px rgba(160,0,255,0.32);}
.gc-17:hover{box-shadow:0 8px 32px rgba(200,100,255,0.55);}
/* --- full-screen container --- */
#game17UI{display:none;position:fixed;inset:0;z-index:90;overflow-y:auto;overscroll-behavior:contain;}
#game17UI.show{display:block;}
/* --- shared back btn --- */
.g17-back-btn{background:rgba(160,60,255,0.18);border:1.5px solid rgba(180,80,255,0.4);color:#cc88ff;font-size:13px;font-weight:800;padding:7px 14px;border-radius:12px;cursor:pointer;transition:background .15s;}
.g17-back-btn:active{transform:scale(.95);}
/* ══════ INTRO SCREEN ══════ */
#g17Intro{min-height:100vh;display:flex;flex-direction:column;align-items:center;background:linear-gradient(180deg,#03000f 0%,#0f0328 55%,#1a0535 100%);overflow:hidden;position:relative;}
.g17-intro-stars{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
.g17-star{position:absolute;border-radius:50%;background:#fff;animation:g17twinkle 2.5s ease-in-out infinite alternate;}
@keyframes g17twinkle{0%{opacity:.15;transform:scale(.8)}100%{opacity:1;transform:scale(1.3)}}
.g17-castle-wrap{width:100%;max-width:520px;flex-shrink:0;}
.g17-castle-svg{width:100%;display:block;}
.g17-intro-body{text-align:center;padding:0 24px 40px;direction:rtl;position:relative;z-index:2;width:100%;max-width:420px;}
.g17-main-title{font-size:30px;font-weight:900;background:linear-gradient(135deg,#ffe57a,#ffd700,#ffb300);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:1px;margin-bottom:4px;line-height:1.2;}
.g17-sub-title{font-size:13px;color:rgba(200,155,255,0.85);font-weight:800;letter-spacing:4px;text-transform:uppercase;margin-bottom:20px;}
.g17-intro-story{font-size:14px;color:rgba(220,200,255,0.82);line-height:1.85;border:1px solid rgba(160,80,255,0.25);border-radius:18px;padding:18px 20px;background:rgba(70,0,130,0.25);margin-bottom:26px;text-align:center;}
.g17-start-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:18px;font-weight:900;padding:16px 52px;border-radius:30px;cursor:pointer;box-shadow:0 6px 28px rgba(180,0,255,0.55);letter-spacing:1px;transition:transform .15s,box-shadow .15s;}
.g17-start-btn:hover{transform:translateY(-2px);box-shadow:0 10px 38px rgba(200,0,255,0.75);}
.g17-start-btn:active{transform:scale(.97);}
/* ══════ SCREEN 1 – GATE ══════ */
#g17S1{display:none;min-height:100vh;flex-direction:column;align-items:center;background:linear-gradient(170deg,#070014 0%,#130330 55%,#0d0028 100%);padding-bottom:48px;direction:rtl;}
#g17S1.show{display:flex;}
.g17-header{width:100%;max-width:480px;display:flex;align-items:center;justify-content:space-between;padding:14px 16px 6px;}
.g17-screen-title{font-size:15px;font-weight:900;color:#ffd700;}
.g17-narration{font-size:13px;color:rgba(215,190,255,0.8);text-align:center;max-width:340px;line-height:1.75;padding:10px 20px 16px;border-bottom:1px solid rgba(160,80,255,0.2);margin-bottom:10px;width:100%;box-sizing:border-box;}
/* scene grid */
.g17-scene{display:grid;grid-template-columns:1fr 160px 1fr;grid-template-rows:1fr 1fr;gap:10px;padding:6px 14px;width:100%;max-width:440px;box-sizing:border-box;}
.g17-item{display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(70,0,130,0.3);border:1.5px solid rgba(160,80,255,0.35);border-radius:18px;padding:12px 6px 10px;cursor:pointer;gap:5px;transition:transform .15s,background .15s,box-shadow .15s;-webkit-tap-highlight-color:transparent;}
.g17-item:hover,.g17-item:active{transform:scale(1.07);background:rgba(110,0,190,0.5);box-shadow:0 4px 20px rgba(180,80,255,0.45);}
.g17-item.checked{border-color:#ffd700;background:rgba(100,70,0,0.35);box-shadow:0 0 14px rgba(255,200,0,0.3);}
.g17-item-icon{font-size:36px;line-height:1.1;}
.g17-item-lbl{font-size:11px;color:rgba(205,170,255,0.9);font-weight:800;text-align:center;}
.g17-gate-cell{grid-column:2;grid-row:1/3;display:flex;align-items:center;justify-content:center;}
.g17-gate-svg{width:100%;max-width:158px;}
/* lock section */
.g17-lock-wrap{width:100%;max-width:380px;display:flex;flex-direction:column;align-items:center;gap:10px;padding:14px 16px;margin-top:4px;}
.g17-code-row{display:flex;gap:10px;align-items:center;direction:ltr;}
.g17-code-input{width:118px;height:52px;background:rgba(10,0,28,0.9);border:2px solid rgba(160,80,255,0.7);border-radius:14px;color:#ffd700;font-size:28px;font-weight:900;text-align:center;letter-spacing:8px;outline:none;caret-color:#ffd700;transition:border-color .2s,box-shadow .2s;}
.g17-code-input:focus{border-color:#cc44ff;box-shadow:0 0 18px rgba(200,80,255,0.45);}
.g17-open-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:15px;font-weight:900;padding:14px 22px;border-radius:14px;cursor:pointer;box-shadow:0 4px 18px rgba(160,0,255,0.4);transition:transform .12s;}
.g17-open-btn:active{transform:scale(.95);}
.g17-feedback{font-size:13px;font-weight:800;color:rgba(255,140,140,0.95);text-align:center;min-height:22px;padding:0 20px;direction:rtl;}
.g17-hint-box{font-size:13px;color:rgba(255,215,0,0.8);text-align:center;max-width:290px;padding:10px 16px;background:rgba(70,55,0,0.35);border:1px solid rgba(255,200,0,0.25);border-radius:12px;display:none;direction:rtl;line-height:1.6;}
/* ══════ POPUP ══════ */
#g17Popup{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.78);z-index:210;align-items:center;justify-content:center;padding:20px;box-sizing:border-box;}
#g17Popup.show{display:flex;}
.g17-popup-box{background:linear-gradient(145deg,#170430,#2c006a);border:1.5px solid rgba(200,110,255,0.55);border-radius:26px;max-width:320px;width:100%;padding:28px 22px 22px;text-align:center;position:relative;box-shadow:0 10px 48px rgba(160,0,255,0.5);direction:rtl;}
.g17-popup-icon{font-size:54px;margin-bottom:12px;line-height:1;}
.g17-popup-name{font-size:13px;color:rgba(200,155,255,0.75);font-weight:800;margin-bottom:8px;letter-spacing:1px;}
.g17-popup-clue{font-size:15px;color:rgba(230,210,255,0.95);line-height:1.75;margin-bottom:22px;}
.g17-popup-close{background:rgba(160,60,255,0.22);border:1.5px solid rgba(200,110,255,0.45);color:#cc88ff;font-size:14px;font-weight:800;padding:10px 30px;border-radius:14px;cursor:pointer;transition:background .15s;}
.g17-popup-close:hover{background:rgba(160,60,255,0.45);}
/* ══════ SUCCESS OVERLAY ══════ */
#g17Success{display:none;position:fixed;inset:0;background:rgba(2,0,10,0.9);z-index:220;flex-direction:column;align-items:center;justify-content:center;padding:32px 24px;text-align:center;direction:rtl;}
#g17Success.show{display:flex;}
.g17-success-orb{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff9e6,#ffd700,rgba(255,140,0,0));animation:g17orbpulse 1.6s ease-in-out infinite;margin-bottom:22px;display:flex;align-items:center;justify-content:center;font-size:50px;}
@keyframes g17orbpulse{0%,100%{transform:scale(1);box-shadow:0 0 30px rgba(255,215,0,0.5)}50%{transform:scale(1.12);box-shadow:0 0 70px rgba(255,215,0,0.9)}}
.g17-success-hed{font-size:24px;font-weight:900;color:#ffd700;margin-bottom:10px;text-shadow:0 0 20px rgba(255,215,0,0.6);}
.g17-success-body{font-size:15px;color:rgba(220,200,255,0.9);line-height:1.8;max-width:300px;margin-bottom:30px;}
.g17-continue-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(180,0,255,0.55);}
/* gate open animation */
@keyframes g17gateOpen{0%{transform:scaleX(1);opacity:1}100%{transform:scaleX(0);opacity:0}}
.g17-gate-opening .g17-gate-bars{animation:g17gateOpen .9s ease-in forwards;}
@keyframes g17lockGlow{0%,100%{filter:drop-shadow(0 0 4px rgba(255,215,0,0.4))}50%{filter:drop-shadow(0 0 16px rgba(255,215,0,1))}}
.g17-lock-glow{animation:g17lockGlow .5s ease-in-out 3;}
/* gate light burst */
@keyframes g17gateBurst{0%{opacity:0;transform:scaleX(0)}40%{opacity:1}100%{opacity:0;transform:scaleX(1)}}
.g17-gate-light{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(255,220,100,0.7) 0%,transparent 70%);animation:g17gateBurst 1.2s ease-out forwards;pointer-events:none;border-radius:inherit;}
"""

if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_ANCHOR + CSS_NEW, 1)
    print("CSS OK")
else:
    print("ERROR: CSS anchor not found")

# ─────────────────────────────────────────────────────────────────
# 2. CATEGORY + CARD (after עוד משחקים section)
# ─────────────────────────────────────────────────────────────────
CAT_ANCHOR = '            </div>\n          </div>\n        </div>\n\n      </div>\n    </div>\n\n    <!-- Ignisia right ads -->'
CAT_NEW = '''            </div>
          </div>
        </div>

        <!-- ══ חדר בריחה ══ -->
        <div class="cat-section">
          <div class="cat-header">
            <div class="cat-line"></div>
            <span class="cat-title">🏰 חדר בריחה</span>
            <div class="cat-line"></div>
          </div>
          <div class="cat-grid cat-grid-2">
            <div class="game-card gc-17" onclick="startFromCard(17)">
              <div class="card-num-badge">16</div>
              <span class="card-icon">🔮</span>
              <div class="card-name">הנסיכה הקסומה</div>
              <div class="card-desc">פענח את סימני האגדות ופתח את שער הממלכה</div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Ignisia right ads -->'''

if CAT_ANCHOR in content:
    content = content.replace(CAT_ANCHOR, CAT_NEW, 1)
    print("Category OK")
else:
    print("ERROR: Category anchor not found — trying fallback")
    # fallback: look for simpler pattern
    fallback = '      </div>\n    </div>\n\n    <!-- Ignisia right ads -->'
    if fallback in content:
        content = content.replace(fallback,
            '\n        <!-- ══ חדר בריחה ══ -->\n'
            '        <div class="cat-section">\n'
            '          <div class="cat-header">\n'
            '            <div class="cat-line"></div>\n'
            '            <span class="cat-title">🏰 חדר בריחה</span>\n'
            '            <div class="cat-line"></div>\n'
            '          </div>\n'
            '          <div class="cat-grid cat-grid-2">\n'
            '            <div class="game-card gc-17" onclick="startFromCard(17)">\n'
            '              <div class="card-num-badge">16</div>\n'
            '              <span class="card-icon">🔮</span>\n'
            '              <div class="card-name">הנסיכה הקסומה</div>\n'
            '              <div class="card-desc">פענח את סימני האגדות ופתח את שער הממלכה</div>\n'
            '            </div>\n'
            '          </div>\n'
            '        </div>\n\n'
            '      </div>\n    </div>\n\n    <!-- Ignisia right ads -->', 1)
        print("Category fallback OK")
    else:
        print("ERROR: fallback also failed")

# ─────────────────────────────────────────────────────────────────
# 3. GAME HTML (before BREAK MODAL)
# ─────────────────────────────────────────────────────────────────
HTML_ANCHOR = '<!-- ══ GAME 16 – מיקס מילים ══ -->'

GAME_HTML = '''<!-- ══ GAME 17 – הנסיכה הקסומה ══ -->
<div id="game17UI">

  <!-- ── INTRO SCREEN ── -->
  <div id="g17Intro">
    <div class="g17-intro-stars" id="g17Stars"></div>

    <div class="g17-castle-wrap">
      <svg class="g17-castle-svg" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="g17sky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#020009"/>
            <stop offset="45%" stop-color="#0f0328"/>
            <stop offset="100%" stop-color="#1a0535"/>
          </linearGradient>
          <radialGradient id="g17moonhalo" cx="75%" cy="20%" r="25%">
            <stop offset="0%" stop-color="rgba(255,245,180,0.35)"/>
            <stop offset="100%" stop-color="transparent"/>
          </radialGradient>
          <radialGradient id="g17moonface" cx="42%" cy="38%" r="50%">
            <stop offset="0%" stop-color="#fffde8"/>
            <stop offset="65%" stop-color="#ffe082"/>
            <stop offset="100%" stop-color="#ffc107"/>
          </radialGradient>
          <radialGradient id="g17win1" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#fff9c4"/>
            <stop offset="100%" stop-color="#ffa726"/>
          </radialGradient>
          <filter id="g17glow" x="-60%" y="-60%" width="220%" height="220%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
            <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
          <filter id="g17wglow" x="-120%" y="-120%" width="340%" height="340%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/>
            <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>
        <!-- Sky -->
        <rect width="400" height="260" fill="url(#g17sky)"/>
        <!-- Moon halo -->
        <circle cx="300" cy="52" r="52" fill="url(#g17moonhalo)"/>
        <!-- Moon -->
        <circle cx="300" cy="52" r="26" fill="url(#g17moonface)" filter="url(#g17glow)"/>
        <circle cx="293" cy="46" r="4" fill="rgba(0,0,0,0.09)"/>
        <circle cx="308" cy="57" r="3" fill="rgba(0,0,0,0.07)"/>
        <!-- Stars -->
        <circle cx="30" cy="20" r="1.5" fill="#fff" opacity=".8"/>
        <circle cx="65" cy="11" r="1" fill="#fff" opacity=".6"/>
        <circle cx="110" cy="26" r="1.5" fill="#fff" opacity=".9"/>
        <circle cx="148" cy="9" r="1" fill="#fff" opacity=".7"/>
        <circle cx="182" cy="19" r="2" fill="#ffe082" opacity=".75"/>
        <circle cx="222" cy="13" r="1" fill="#fff" opacity=".6"/>
        <circle cx="252" cy="31" r="1.5" fill="#fff" opacity=".7"/>
        <circle cx="356" cy="16" r="1" fill="#fff" opacity=".8"/>
        <circle cx="386" cy="36" r="1.5" fill="#fff" opacity=".6"/>
        <circle cx="50" cy="46" r="1" fill="#fff" opacity=".5"/>
        <circle cx="15" cy="62" r="1.5" fill="#fff" opacity=".65"/>
        <circle cx="372" cy="62" r="1" fill="#fff" opacity=".6"/>
        <circle cx="79" cy="56" r="1" fill="#fff" opacity=".4"/>
        <circle cx="166" cy="42" r="1" fill="#ffe082" opacity=".55"/>
        <circle cx="330" cy="86" r="1" fill="#fff" opacity=".45"/>
        <circle cx="18" cy="88" r="1" fill="#fff" opacity=".4"/>
        <circle cx="390" cy="90" r="1.5" fill="#fff" opacity=".5"/>
        <!-- Ground -->
        <ellipse cx="200" cy="255" rx="240" ry="28" fill="#0a001a"/>
        <!-- Left wall -->
        <rect x="32" y="158" width="336" height="102" fill="#14072e"/>
        <!-- Left tower -->
        <rect x="26" y="128" width="74" height="102" fill="#130630"/>
        <rect x="21" y="116" width="84" height="17" fill="#180a3a"/>
        <rect x="23" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="46" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="69" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="87" y="105" width="15" height="14" fill="#180a3a"/>
        <!-- Center tower (tallest) -->
        <rect x="150" y="58" width="100" height="172" fill="#1a0c3e"/>
        <rect x="144" y="46" width="112" height="17" fill="#1e1046"/>
        <rect x="146" y="33" width="17" height="16" fill="#1e1046"/>
        <rect x="171" y="33" width="17" height="16" fill="#1e1046"/>
        <rect x="196" y="33" width="17" height="16" fill="#1e1046"/>
        <rect x="221" y="33" width="17" height="16" fill="#1e1046"/>
        <rect x="239" y="33" width="17" height="16" fill="#1e1046"/>
        <!-- Center spire -->
        <polygon points="200,8 179,44 221,44" fill="#220e4c"/>
        <!-- Right tower -->
        <rect x="300" y="128" width="74" height="102" fill="#130630"/>
        <rect x="295" y="116" width="84" height="17" fill="#180a3a"/>
        <rect x="297" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="320" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="343" y="105" width="15" height="14" fill="#180a3a"/>
        <rect x="362" y="105" width="15" height="14" fill="#180a3a"/>
        <!-- Gate arch -->
        <path d="M154,260 L154,178 Q200,140 246,178 L246,260 Z" fill="#07000e"/>
        <!-- Gate bars -->
        <line x1="165" y1="188" x2="165" y2="260" stroke="#1a0832" stroke-width="5"/>
        <line x1="179" y1="182" x2="179" y2="260" stroke="#1a0832" stroke-width="5"/>
        <line x1="192" y1="178" x2="192" y2="260" stroke="#1a0832" stroke-width="5"/>
        <line x1="208" y1="178" x2="208" y2="260" stroke="#1a0832" stroke-width="5"/>
        <line x1="221" y1="182" x2="221" y2="260" stroke="#1a0832" stroke-width="5"/>
        <line x1="235" y1="188" x2="235" y2="260" stroke="#1a0832" stroke-width="5"/>
        <!-- Glowing windows -->
        <rect x="52" y="142" width="22" height="28" rx="3" fill="url(#g17win1)" filter="url(#g17wglow)" opacity=".85"/>
        <rect x="104" y="168" width="19" height="24" rx="2" fill="#ffa726" filter="url(#g17wglow)" opacity=".65"/>
        <rect x="170" y="72" width="19" height="25" rx="2" fill="url(#g17win1)" filter="url(#g17wglow)" opacity=".9"/>
        <rect x="211" y="72" width="19" height="25" rx="2" fill="url(#g17win1)" filter="url(#g17wglow)" opacity=".85"/>
        <rect x="170" y="112" width="19" height="24" rx="2" fill="#ffb300" filter="url(#g17wglow)" opacity=".7"/>
        <rect x="211" y="112" width="19" height="24" rx="2" fill="#ffb300" filter="url(#g17wglow)" opacity=".65"/>
        <rect x="277" y="168" width="19" height="24" rx="2" fill="#ffa726" filter="url(#g17wglow)" opacity=".65"/>
        <rect x="326" y="142" width="22" height="28" rx="3" fill="url(#g17win1)" filter="url(#g17wglow)" opacity=".85"/>
        <!-- ground glow -->
        <ellipse cx="200" cy="257" rx="55" ry="7" fill="rgba(140,60,255,0.18)"/>
      </svg>
    </div>

    <div class="g17-intro-body">
      <div class="g17-main-title">הנסיכה הקסומה</div>
      <div class="g17-sub-title">✦ חדר הבריחה ✦</div>
      <div class="g17-intro-story">
        ברוכים הבאים לחדר הבריחה של הנסיכה הקסומה.<br>
        רק מי שיפענח את סימני האגדות…<br>יוכל להיכנס אל הממלכה.
      </div>
      <button class="g17-start-btn" onclick="g17StartPuzzle()">✨ התחל מסע</button>
    </div>
  </div>

  <!-- ── SCREEN 1 – THE GATE ── -->
  <div id="g17S1">
    <div class="g17-header">
      <button class="g17-back-btn" onclick="g17GoBack()">⬅ חזור</button>
      <div class="g17-screen-title">🔒 שער הכניסה</div>
      <div style="width:70px"></div>
    </div>
    <div class="g17-narration">
      ארבע אגדות השאירו כאן סימן.<br>
      כל סימן מסתיר ספרה אחת.<br>
      מצא את הקוד ופתח את השער.
    </div>

    <div class="g17-scene">
      <!-- Top-left: Apple (Snow White) -->
      <div class="g17-item" id="g17item-apple" onclick="g17OpenClue('apple')">
        <div class="g17-item-icon">🍎</div>
        <div class="g17-item-lbl">תפוח</div>
      </div>

      <!-- CENTER: Gate (spans 2 rows) -->
      <div class="g17-gate-cell">
        <div style="position:relative;width:100%;">
          <svg class="g17-gate-svg" viewBox="0 0 160 260" xmlns="http://www.w3.org/2000/svg" id="g17GateSvg">
            <defs>
              <linearGradient id="g17st" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#28145a"/>
                <stop offset="50%" stop-color="#3c2080"/>
                <stop offset="100%" stop-color="#28145a"/>
              </linearGradient>
              <linearGradient id="g17bar" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#281a4a"/>
                <stop offset="50%" stop-color="#483568"/>
                <stop offset="100%" stop-color="#281a4a"/>
              </linearGradient>
            </defs>
            <!-- Outer arch stone -->
            <path d="M8,260 L8,106 Q80,22 152,106 L152,260 Z" fill="url(#g17st)" stroke="#5a3a90" stroke-width="2"/>
            <!-- Stone seam lines -->
            <line x1="8" y1="142" x2="38" y2="142" stroke="#4a2a70" stroke-width="1"/>
            <line x1="122" y1="142" x2="152" y2="142" stroke="#4a2a70" stroke-width="1"/>
            <line x1="8" y1="178" x2="33" y2="178" stroke="#4a2a70" stroke-width="1"/>
            <line x1="127" y1="178" x2="152" y2="178" stroke="#4a2a70" stroke-width="1"/>
            <line x1="8" y1="214" x2="28" y2="214" stroke="#4a2a70" stroke-width="1"/>
            <line x1="132" y1="214" x2="152" y2="214" stroke="#4a2a70" stroke-width="1"/>
            <!-- Inner arch dark -->
            <path d="M28,260 L28,114 Q80,44 132,114 L132,260 Z" fill="#05000c"/>
            <!-- Iron bars group (will be animated) -->
            <g id="g17Bars" class="g17-gate-bars">
              <rect x="36" y="126" width="10" height="134" rx="5" fill="url(#g17bar)"/>
              <rect x="54" y="119" width="10" height="141" rx="5" fill="url(#g17bar)"/>
              <rect x="72" y="116" width="10" height="144" rx="5" fill="url(#g17bar)"/>
              <rect x="90" y="116" width="10" height="144" rx="5" fill="url(#g17bar)"/>
              <rect x="108" y="119" width="10" height="141" rx="5" fill="url(#g17bar)"/>
              <rect x="126" y="126" width="10" height="134" rx="5" fill="url(#g17bar)"/>
              <!-- Spikes -->
              <polygon points="41,126 36,111 46,111" fill="#5a3a90"/>
              <polygon points="59,119 54,104 64,104" fill="#5a3a90"/>
              <polygon points="77,116 72,101 82,101" fill="#5a3a90"/>
              <polygon points="95,116 90,101 100,101" fill="#5a3a90"/>
              <polygon points="113,119 108,104 118,104" fill="#5a3a90"/>
              <polygon points="131,126 126,111 136,111" fill="#5a3a90"/>
              <!-- Crossbar -->
              <rect x="31" y="172" width="98" height="10" rx="4" fill="#3a2a60" stroke="#5a4080" stroke-width="1"/>
            </g>
            <!-- Lock -->
            <g id="g17LockGroup">
              <rect x="66" y="155" width="28" height="20" rx="5" fill="#1a1000" stroke="#ffd700" stroke-width="1.5" id="g17LockBody"/>
              <path d="M70,155 L70,146 Q80,136 90,146 L90,155" fill="none" stroke="#ffd700" stroke-width="2.2" id="g17LockShackle"/>
              <circle cx="80" cy="163" r="4" fill="#04000a"/>
              <rect x="78" y="165" width="4" height="6" rx="1.5" fill="#04000a"/>
            </g>
          </svg>
        </div>
      </div>

      <!-- Top-right: Love Letter (Romeo & Juliet) -->
      <div class="g17-item" id="g17item-letter" onclick="g17OpenClue('letter')">
        <div class="g17-item-icon">💌</div>
        <div class="g17-item-lbl">מכתב אהבה</div>
      </div>

      <!-- Bottom-left: Clock (Cinderella) -->
      <div class="g17-item" id="g17item-clock" onclick="g17OpenClue('clock')">
        <div class="g17-item-icon">🕛</div>
        <div class="g17-item-lbl">שעון חצות</div>
      </div>

      <!-- Bottom-right: Building (Sesame Street / neighbors) -->
      <div class="g17-item" id="g17item-building" onclick="g17OpenClue('building')">
        <div class="g17-item-icon">🏠</div>
        <div class="g17-item-lbl">בניין</div>
      </div>
    </div>

    <div class="g17-lock-wrap">
      <div class="g17-code-row">
        <input class="g17-code-input" id="g17CodeInput" type="tel" maxlength="4" placeholder="????"/>
        <button class="g17-open-btn" onclick="g17CheckCode()">פתח את השער 🔑</button>
      </div>
      <div class="g17-feedback" id="g17Feedback"></div>
      <div class="g17-hint-box" id="g17Hint">
        💡 כל פריט מספר סיפור אחר… אל תחפש תשובה ישירה — אלא <em>משמעות</em>.
      </div>
    </div>
  </div>

  <!-- ── CLUE POPUP ── -->
  <div id="g17Popup">
    <div class="g17-popup-box">
      <div class="g17-popup-icon" id="g17PopupIcon"></div>
      <div class="g17-popup-name" id="g17PopupName"></div>
      <div class="g17-popup-clue" id="g17PopupClue"></div>
      <button class="g17-popup-close" onclick="g17CloseClue()">סגור</button>
    </div>
  </div>

  <!-- ── SUCCESS OVERLAY ── -->
  <div id="g17Success">
    <div class="g17-success-orb">🔓</div>
    <div class="g17-success-hed">השער נפתח…</div>
    <div class="g17-success-body">
      אתה מתחיל להבין את שפת האגדות.<br>
      הממלכה מחכה לך מעבר לשער.
    </div>
    <button class="g17-continue-btn" onclick="g17ContinueBtn()">המשך למסע 🌟</button>
  </div>

</div>

'''

if HTML_ANCHOR in content:
    content = content.replace(HTML_ANCHOR, GAME_HTML + HTML_ANCHOR, 1)
    print("HTML OK")
else:
    print("ERROR: HTML anchor not found — trying BREAK MODAL")
    BM = '<!-- ══ BREAK MODAL ══ -->'
    if BM in content:
        content = content.replace(BM, GAME_HTML + BM, 1)
        print("HTML fallback OK")
    else:
        print("ERROR: HTML fallback also failed")

# ─────────────────────────────────────────────────────────────────
# 4. ROUTING
# ─────────────────────────────────────────────────────────────────
ROUTE_ANCHOR = '  if(lvl===16){startGame16();return;}'
ROUTE_NEW = '  if(lvl===16){startGame16();return;}\n  if(lvl===17){startGame17();return;}'
if ROUTE_ANCHOR in content:
    content = content.replace(ROUTE_ANCHOR, ROUTE_NEW, 1)
    print("Routing OK")
else:
    print("ERROR: Routing anchor not found")

# ─────────────────────────────────────────────────────────────────
# 5. CLEANUP IN hideGame
# ─────────────────────────────────────────────────────────────────
HIDE_ANCHOR = '  g16ExitToMenu&&g16ExitToMenu(true);'
HIDE_NEW = '  g16ExitToMenu&&g16ExitToMenu(true);\n  g17ExitToMenu&&g17ExitToMenu(true);'
if HIDE_ANCHOR in content:
    content = content.replace(HIDE_ANCHOR, HIDE_NEW, 1)
    print("Cleanup OK")
else:
    print("ERROR: Cleanup anchor not found")

# ─────────────────────────────────────────────────────────────────
# 6. JAVASCRIPT
# ─────────────────────────────────────────────────────────────────
JS_ANCHOR = '</script>\n</body>'

GAME_JS = r"""
/* ═══════════════════════════════════════════════
   GAME 17 – הנסיכה הקסומה – חדר הבריחה
   ═══════════════════════════════════════════════ */
let g17ExitToMenu = null;
let g17WrongCount = 0;

const G17_CLUES = {
  apple:    { icon:'🍎', name:'שלגיה',           clue:'מי שליווה אותה ביער לא היה אחד… כמה היו?' },
  letter:   { icon:'💌', name:'רומיאו ויוליה',    clue:'סיפור אהבה אחד… שני לבבות… גורל אחד.\n\nכמה היה?' },
  clock:    { icon:'🕛', name:'סינדרלה',          clue:'ברגע שהשעון היכה חצות, הקסם נעלם.\nחבר את ספרות השעה שבה הכל השתנה.' },
  building: { icon:'🏠', name:'דירה להשכיר',      clue:'בבניין אחד חיפשו שכן חדש.\nכמה דיירים כבר גרו שם?' }
};
const G17_CODE = '7235';

function startGame17() {
  if (g17ExitToMenu) g17ExitToMenu(false);
  var ui = document.getElementById('game17UI');
  g17WrongCount = 0;
  // reset state
  document.getElementById('g17CodeInput').value = '';
  document.getElementById('g17Feedback').textContent = '';
  document.getElementById('g17Hint').style.display = 'none';
  ['apple','letter','clock','building'].forEach(function(k){
    var el = document.getElementById('g17item-'+k);
    if(el) el.classList.remove('checked');
  });
  document.getElementById('g17Success').classList.remove('show');
  document.getElementById('g17Popup').classList.remove('show');
  // restore bars opacity
  var bars = document.getElementById('g17Bars');
  if (bars) { bars.style.opacity='1'; bars.style.transform=''; }
  // show intro
  document.getElementById('g17Intro').style.display = 'flex';
  document.getElementById('g17S1').classList.remove('show');

  g17ExitToMenu = function(silent) {
    g17ExitToMenu = null;
    if (!silent) { hideGame(); navTo('mainPage'); }
  };
  ui.classList.add('show');
  navTo('game17UI');
  g17MakeStars();
}

function g17MakeStars() {
  var wrap = document.getElementById('g17Stars');
  if (!wrap) return;
  wrap.innerHTML = '';
  for (var i = 0; i < 28; i++) {
    var s = document.createElement('div');
    s.className = 'g17-star';
    var sz = 1.5 + Math.random() * 2.5;
    s.style.cssText = 'width:'+sz+'px;height:'+sz+'px;top:'+(Math.random()*70)+'%;left:'+(Math.random()*100)+'%;animation-delay:'+(Math.random()*3)+'s;animation-duration:'+(2+Math.random()*2)+'s;';
    wrap.appendChild(s);
  }
}

function g17StartPuzzle() {
  document.getElementById('g17Intro').style.display = 'none';
  document.getElementById('g17S1').classList.add('show');
}

function g17GoBack() {
  if (g17ExitToMenu) g17ExitToMenu(false);
  else { hideGame(); navTo('mainPage'); }
}

function g17OpenClue(item) {
  var data = G17_CLUES[item];
  if (!data) return;
  document.getElementById('g17PopupIcon').textContent = data.icon;
  document.getElementById('g17PopupName').textContent = data.name;
  document.getElementById('g17PopupClue').textContent = data.clue;
  document.getElementById('g17Popup').classList.add('show');
  // mark item as checked
  var el = document.getElementById('g17item-'+item);
  if (el) el.classList.add('checked');
}

function g17CloseClue() {
  document.getElementById('g17Popup').classList.remove('show');
}

function g17CheckCode() {
  var val = document.getElementById('g17CodeInput').value.trim();
  var fb = document.getElementById('g17Feedback');
  if (val.length < 4) {
    fb.textContent = 'הכנס 4 ספרות כדי לפתוח את השער.';
    fb.style.color = 'rgba(255,200,100,0.9)';
    return;
  }
  if (val === G17_CODE) {
    g17OpenGate();
  } else {
    g17WrongCount++;
    if (g17WrongCount >= 2) {
      document.getElementById('g17Hint').style.display = 'block';
    }
    fb.style.color = 'rgba(255,130,130,0.95)';
    fb.textContent = 'השער רעד… אבל לא נפתח. אחת האגדות עדיין מסתירה ממך את הסוד.';
    // shake input
    var inp = document.getElementById('g17CodeInput');
    inp.style.animation = 'none';
    inp.style.borderColor = '#ff4444';
    setTimeout(function(){
      inp.style.borderColor = '';
      inp.style.animation = '';
    }, 600);
    document.getElementById('g17CodeInput').value = '';
  }
}

function g17OpenGate() {
  // lock glow
  var lock = document.getElementById('g17LockGroup');
  if (lock) lock.style.filter = 'drop-shadow(0 0 12px rgba(255,215,0,1))';
  document.getElementById('g17Feedback').textContent = '';
  document.getElementById('g17Hint').style.display = 'none';
  // fade out bars
  var bars = document.getElementById('g17Bars');
  if (bars) {
    bars.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    bars.style.opacity = '0';
    bars.style.transform = 'scaleX(0)';
  }
  // after animation show success
  setTimeout(function() {
    document.getElementById('g17Success').classList.add('show');
  }, 1100);
}

function g17ContinueBtn() {
  // No next screen yet — just close gracefully
  document.getElementById('g17Success').classList.remove('show');
  g17GoBack();
}
"""

if JS_ANCHOR in content:
    content = content.replace(JS_ANCHOR, GAME_JS + JS_ANCHOR, 1)
    print("JS OK")
else:
    print("ERROR: JS anchor not found")

# ─────────────────────────────────────────────────────────────────
# WRITE
# ─────────────────────────────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
new_len = len(content)
print(f"Done! New length: {new_len}  (+{new_len - orig_len})")
