# -*- coding: utf-8 -*-
filepath = '/sessions/bold-confident-feynman/mnt/outputs/כובש_השטחים.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
orig = len(content)
print(f"Original: {orig}")

# ─────────────────────────────────────────────────────────────────
# 1.  CSS for Screen 2
# ─────────────────────────────────────────────────────────────────
CSS_ANCHOR = '.g17-gate-light{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(255,220,100,0.7) 0%,transparent 70%);animation:g17gateBurst 1.2s ease-out forwards;pointer-events:none;border-radius:inherit;}'
CSS_NEW = CSS_ANCHOR + r"""
/* ══════ TRANSITION SCREEN ══════ */
#g17Trans{display:none;min-height:100vh;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(170deg,#020008 0%,#0d0228 60%,#180430 100%);padding:40px 28px;text-align:center;direction:rtl;}
#g17Trans.show{display:flex;}
.g17-trans-icon{font-size:64px;margin-bottom:22px;animation:g17transFloat 3s ease-in-out infinite;}
@keyframes g17transFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.g17-trans-text{font-size:16px;color:rgba(215,190,255,0.88);line-height:1.85;max-width:320px;border:1px solid rgba(160,80,255,0.25);border-radius:18px;padding:20px 22px;background:rgba(60,0,120,0.28);margin-bottom:32px;}
.g17-trans-btn{background:linear-gradient(135deg,#6600aa,#bb0099);border:none;color:#fff;font-size:17px;font-weight:900;padding:16px 50px;border-radius:28px;cursor:pointer;box-shadow:0 6px 28px rgba(160,0,220,0.55);transition:transform .15s;}
.g17-trans-btn:active{transform:scale(.96);}
/* ══════ SCREEN 2 – MIRRORS ROOM ══════ */
#g17S2{display:none;min-height:100vh;flex-direction:column;align-items:center;background:linear-gradient(170deg,#050010 0%,#100225 55%,#080018 100%);padding-bottom:48px;direction:rtl;}
#g17S2.show{display:flex;}
.g17-s2-narration{font-size:13px;color:rgba(200,175,255,0.78);text-align:center;max-width:340px;line-height:1.75;padding:10px 20px 16px;border-bottom:1px solid rgba(140,70,255,0.2);margin-bottom:16px;width:100%;box-sizing:border-box;}
/* 4 mirrors grid */
.g17-mirrors-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:0 16px;width:100%;max-width:420px;box-sizing:border-box;margin-bottom:16px;}
.g17-mirror{position:relative;background:linear-gradient(160deg,#08001c,#140435,#0a0020);border-radius:50% 50% 46% 46% / 55% 55% 45% 45%;border:2px solid rgba(160,80,255,0.45);padding:18px 10px 22px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;cursor:default;transition:box-shadow .4s,border-color .4s;min-height:120px;overflow:hidden;}
.g17-mirror::before{content:'';position:absolute;inset:0;border-radius:inherit;background:linear-gradient(145deg,rgba(200,140,255,0.06) 0%,transparent 60%);pointer-events:none;}
.g17-mirror-letters{font-size:22px;font-weight:900;color:rgba(220,190,255,0.9);letter-spacing:4px;font-family:monospace;text-shadow:0 0 12px rgba(180,100,255,0.6);}
.g17-mirror-num{font-size:11px;color:rgba(180,140,255,0.45);font-weight:700;letter-spacing:1px;}
/* lit state (success) */
.g17-mirror.lit{border-color:rgba(255,215,0,0.9);box-shadow:0 0 28px rgba(255,200,0,0.7),0 0 60px rgba(255,160,0,0.3),inset 0 0 20px rgba(255,210,0,0.15);animation:g17mirrorLit .6s ease-out;}
@keyframes g17mirrorLit{0%{transform:scale(1)}40%{transform:scale(1.07)}100%{transform:scale(1)}}
.g17-mirror.lit .g17-mirror-letters{color:#ffd700;text-shadow:0 0 20px rgba(255,215,0,0.9);}
/* central mirror */
.g17-central-wrap{width:100%;max-width:420px;padding:0 16px;box-sizing:border-box;margin-bottom:14px;display:flex;flex-direction:column;align-items:center;}
.g17-central-mirror{width:100%;background:linear-gradient(175deg,#06001a,#140338,#08001c);border-radius:50% 50% 48% 48% / 38% 38% 62% 62%;border:2.5px solid rgba(140,60,255,0.5);padding:28px 16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative;overflow:hidden;min-height:110px;transition:box-shadow .6s,border-color .6s;}
.g17-central-mirror::before{content:'';position:absolute;inset:0;border-radius:inherit;background:linear-gradient(145deg,rgba(200,140,255,0.05) 0%,transparent 55%);pointer-events:none;}
.g17-central-lock{font-size:32px;opacity:.7;}
.g17-central-label{font-size:12px;color:rgba(170,130,255,0.65);font-weight:700;letter-spacing:1.5px;}
.g17-central-mirror.open{border-color:rgba(255,215,0,0.95);box-shadow:0 0 40px rgba(255,210,0,0.8),0 0 90px rgba(255,160,0,0.4),inset 0 0 40px rgba(255,220,0,0.2);}
.g17-central-mirror.open .g17-central-lock{font-size:36px;opacity:1;animation:g17lockUnlock .5s ease-out;}
@keyframes g17lockUnlock{0%{transform:scale(1) rotate(0)}50%{transform:scale(1.3) rotate(-15deg)}100%{transform:scale(1) rotate(0)}}
/* code row s2 */
.g17-s2-lock-wrap{display:flex;flex-direction:column;align-items:center;gap:10px;padding:0 16px;width:100%;max-width:380px;box-sizing:border-box;}
.g17-s2-code-row{display:flex;gap:10px;align-items:center;direction:ltr;}
.g17-s2-input{width:96px;height:52px;background:rgba(6,0,18,0.9);border:2px solid rgba(140,70,255,0.7);border-radius:14px;color:#ffd700;font-size:28px;font-weight:900;text-align:center;letter-spacing:6px;outline:none;caret-color:#ffd700;transition:border-color .2s,box-shadow .2s;}
.g17-s2-input:focus{border-color:#cc44ff;box-shadow:0 0 18px rgba(200,80,255,0.45);}
.g17-s2-open-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:14px;font-weight:900;padding:14px 20px;border-radius:14px;cursor:pointer;box-shadow:0 4px 16px rgba(160,0,255,0.4);transition:transform .12s;}
.g17-s2-open-btn:active{transform:scale(.95);}
.g17-s2-feedback{font-size:13px;font-weight:800;color:rgba(255,130,130,0.95);text-align:center;min-height:22px;direction:rtl;}
.g17-s2-hint{font-size:13px;color:rgba(255,215,0,0.8);text-align:center;max-width:290px;padding:10px 16px;background:rgba(70,55,0,0.32);border:1px solid rgba(255,200,0,0.22);border-radius:12px;display:none;direction:rtl;line-height:1.6;}
/* success 2 */
#g17Success2{display:none;position:fixed;inset:0;background:rgba(2,0,10,0.9);z-index:220;flex-direction:column;align-items:center;justify-content:center;padding:32px 24px;text-align:center;direction:rtl;}
#g17Success2.show{display:flex;}
.g17-s2-success-orb{width:120px;height:120px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff9e6,#ffd700,rgba(255,140,0,0));animation:g17orbpulse 1.6s ease-in-out infinite;margin-bottom:22px;display:flex;align-items:center;justify-content:center;font-size:52px;}
.g17-s2-success-hed{font-size:22px;font-weight:900;color:#ffd700;margin-bottom:10px;text-shadow:0 0 20px rgba(255,215,0,0.6);}
.g17-s2-success-body{font-size:15px;color:rgba(220,200,255,0.9);line-height:1.8;max-width:300px;margin-bottom:28px;}
.g17-s2-continue-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(180,0,255,0.55);}
"""
if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_NEW, 1)
    print("CSS OK")
else:
    print("ERROR: CSS anchor not found")

# ─────────────────────────────────────────────────────────────────
# 2.  HTML – Transition + Screen 2 (insert before closing </div> of game17UI)
# ─────────────────────────────────────────────────────────────────
HTML_ANCHOR = '    <button class="g17-continue-btn" onclick="g17ContinueBtn()">המשך למסע 🌟</button>\n  </div>\n\n</div>\n\n<!-- ══ GAME 16'
HTML_NEW = '''    <button class="g17-continue-btn" onclick="g17ContinueBtn()">המשך למסע 🌟</button>
  </div>

  <!-- ── TRANSITION ── -->
  <div id="g17Trans">
    <div class="g17-trans-icon">🌟</div>
    <div class="g17-trans-text">
      השער נפתח באור זהוב… אבל זה היה רק חימום.<br><br>
      כדי להגיע אל הנסיכה, תצטרך להרכיב את האמת מתוך השברים.
    </div>
    <button class="g17-trans-btn" onclick="g17EnterMirrors()">כניסה לחדר המראות 🪞</button>
  </div>

  <!-- ── SCREEN 2 – MIRRORS ROOM ── -->
  <div id="g17S2">
    <div class="g17-header">
      <button class="g17-back-btn" onclick="g17GoBack()">⬅ חזור</button>
      <div class="g17-screen-title">🪞 חדר המראות</div>
      <div style="width:70px"></div>
    </div>
    <div class="g17-s2-narration">
      המראות פיזרו את הסוד לחלקים.<br>
      רק מי שיסדר נכון את מה שנשבר — יוכל להמשיך.
    </div>

    <div class="g17-mirrors-grid">
      <div class="g17-mirror" id="g17m1">
        <div class="g17-mirror-letters">NEELEV</div>
        <div class="g17-mirror-num">מראה א׳</div>
      </div>
      <div class="g17-mirror" id="g17m2">
        <div class="g17-mirror-letters">YTWENT</div>
        <div class="g17-mirror-num">מראה ב׳</div>
      </div>
      <div class="g17-mirror" id="g17m3">
        <div class="g17-mirror-letters">EHTER</div>
        <div class="g17-mirror-num">מראה ג׳</div>
      </div>
      <div class="g17-mirror" id="g17m4">
        <div class="g17-mirror-letters">VNESE</div>
        <div class="g17-mirror-num">מראה ד׳</div>
      </div>
    </div>

    <div class="g17-central-wrap">
      <div class="g17-central-mirror" id="g17CentralMirror">
        <div class="g17-central-lock">🔒</div>
        <div class="g17-central-label">מראה המרכז — נעולה</div>
      </div>
    </div>

    <div class="g17-s2-lock-wrap">
      <div class="g17-s2-code-row">
        <input class="g17-s2-input" id="g17S2Code" type="tel" maxlength="2" placeholder="??"/>
        <button class="g17-s2-open-btn" onclick="g17CheckS2()">פתח את המראה 🔑</button>
      </div>
      <div class="g17-s2-feedback" id="g17S2Feedback"></div>
      <div class="g17-s2-hint" id="g17S2Hint">
        💡 המראות לא מציגות מילים שלמות… אבל כל שבר מסתיר מספר.
      </div>
    </div>
  </div>

  <!-- ── SUCCESS 2 ── -->
  <div id="g17Success2">
    <div class="g17-s2-success-orb">🪞</div>
    <div class="g17-s2-success-hed">הצלחת להרכיב את הסוד.</div>
    <div class="g17-s2-success-body">
      המראה נפתחת… והדרך אל הנסיכה ממשיכה.
    </div>
    <button class="g17-s2-continue-btn" onclick="g17S2ContinueBtn()">המשך למסע 🌟</button>
  </div>

</div>

<!-- ══ GAME 16'''
if HTML_ANCHOR in content:
    content = content.replace(HTML_ANCHOR, HTML_NEW, 1)
    print("HTML OK")
else:
    print("ERROR: HTML anchor not found")
    # debug
    idx = content.find('g17ContinueBtn()">המשך למסע')
    print(f"  Button found at: {idx}")
    if idx > 0: print(repr(content[idx:idx+120]))

# ─────────────────────────────────────────────────────────────────
# 3.  JS – replace g17ContinueBtn + add all Screen 2 functions
# ─────────────────────────────────────────────────────────────────
OLD_JS = r"""function g17ContinueBtn() {
  // No next screen yet — just close gracefully
  document.getElementById('g17Success').classList.remove('show');
  g17GoBack();
}"""
NEW_JS = r"""function g17ContinueBtn() {
  document.getElementById('g17Success').classList.remove('show');
  // show transition screen
  var t = document.getElementById('g17Trans');
  t.classList.add('show');
  document.getElementById('g17S1').classList.remove('show');
  document.getElementById('g17Intro').style.display = 'none';
}

function g17EnterMirrors() {
  document.getElementById('g17Trans').classList.remove('show');
  // reset screen 2
  g17S2WrongCount = 0;
  document.getElementById('g17S2Code').value = '';
  document.getElementById('g17S2Feedback').textContent = '';
  document.getElementById('g17S2Hint').style.display = 'none';
  document.getElementById('g17Success2').classList.remove('show');
  ['g17m1','g17m2','g17m3','g17m4'].forEach(function(id){
    document.getElementById(id).classList.remove('lit');
  });
  var cm = document.getElementById('g17CentralMirror');
  cm.classList.remove('open');
  cm.querySelector('.g17-central-lock').textContent = '🔒';
  cm.querySelector('.g17-central-label').textContent = 'מראה המרכז — נעולה';
  document.getElementById('g17S2').classList.add('show');
}

let g17S2WrongCount = 0;
const G17_CODE2 = '41';

function g17CheckS2() {
  var val = document.getElementById('g17S2Code').value.trim();
  var fb = document.getElementById('g17S2Feedback');
  if (!val) {
    fb.style.color = 'rgba(255,200,100,0.9)';
    fb.textContent = 'הכנס את הקוד כדי לפתוח את המראה.';
    return;
  }
  if (val === G17_CODE2) {
    g17MirrorsSuccess();
  } else {
    g17S2WrongCount++;
    if (g17S2WrongCount >= 2) {
      document.getElementById('g17S2Hint').style.display = 'block';
    }
    fb.style.color = 'rgba(255,130,130,0.95)';
    fb.textContent = 'המראה רעדה… אבל לא נפתחה. הסוד עדיין לא הורכב נכון.';
    var inp = document.getElementById('g17S2Code');
    inp.style.borderColor = '#ff4444';
    setTimeout(function(){ inp.style.borderColor = ''; }, 700);
    document.getElementById('g17S2Code').value = '';
  }
}

function g17MirrorsSuccess() {
  document.getElementById('g17S2Feedback').textContent = '';
  document.getElementById('g17S2Hint').style.display = 'none';
  var mirrors = ['g17m1','g17m2','g17m3','g17m4'];
  mirrors.forEach(function(id, i) {
    setTimeout(function(){
      document.getElementById(id).classList.add('lit');
    }, i * 320);
  });
  // central mirror opens after all 4 light up
  setTimeout(function(){
    var cm = document.getElementById('g17CentralMirror');
    cm.classList.add('open');
    cm.querySelector('.g17-central-lock').textContent = '🔓';
    cm.querySelector('.g17-central-label').textContent = 'המראה נפתחת…';
  }, mirrors.length * 320 + 400);
  // show success overlay
  setTimeout(function(){
    document.getElementById('g17Success2').classList.add('show');
  }, mirrors.length * 320 + 1400);
}

function g17S2ContinueBtn() {
  // No screen 3 yet — close gracefully
  document.getElementById('g17Success2').classList.remove('show');
  g17GoBack();
}"""

if OLD_JS in content:
    content = content.replace(OLD_JS, NEW_JS, 1)
    print("JS OK")
else:
    print("ERROR: JS anchor not found")
    idx = content.find('function g17ContinueBtn()')
    print(f"  g17ContinueBtn found at: {idx}")
    if idx > 0: print(repr(content[idx:idx+80]))

# ─────────────────────────────────────────────────────────────────
# 4.  Also reset g17Trans on startGame17 re-entry
# ─────────────────────────────────────────────────────────────────
OLD_RESET = "  document.getElementById('g17Intro').style.display = 'flex';\n  document.getElementById('g17S1').classList.remove('show');"
NEW_RESET = "  document.getElementById('g17Intro').style.display = 'flex';\n  document.getElementById('g17S1').classList.remove('show');\n  var g17t = document.getElementById('g17Trans'); if(g17t) g17t.classList.remove('show');\n  var g17s2 = document.getElementById('g17S2'); if(g17s2) g17s2.classList.remove('show');\n  var g17s2ov = document.getElementById('g17Success2'); if(g17s2ov) g17s2ov.classList.remove('show');"
if OLD_RESET in content:
    content = content.replace(OLD_RESET, NEW_RESET, 1)
    print("Reset OK")
else:
    print("WARN: reset anchor not found (non-critical)")

# ─────────────────────────────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done. {orig} → {len(content)} (+{len(content)-orig})")
