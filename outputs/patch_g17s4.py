# -*- coding: utf-8 -*-
filepath = '/sessions/bold-confident-feynman/mnt/outputs/כובש_השטחים.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
orig = len(content)
print(f"Original: {orig}")

# ─────────────────────────────────────────────────────────────────
# 1.  CSS
# ─────────────────────────────────────────────────────────────────
CSS_ANCHOR = '.g17-s2-continue-btn{background:linear-gradient(135deg,#7700bb,#c400a0);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(180,0,255,0.55);}'
CSS_NEW = CSS_ANCHOR + r"""
/* ══════ SCREEN 4 – TIME ROOM ══════ */
#g17Trans4{display:none;min-height:100vh;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(170deg,#0d0500 0%,#1e0d02 55%,#120800 100%);padding:40px 28px;text-align:center;direction:rtl;}
#g17Trans4.show{display:flex;}
.g17-t4-icon{font-size:64px;margin-bottom:20px;animation:g17transFloat 3s ease-in-out infinite;}
.g17-t4-trans-text{font-size:15px;color:rgba(255,215,160,0.85);line-height:1.85;max-width:320px;border:1px solid rgba(200,130,0,0.28);border-radius:18px;padding:20px 22px;background:rgba(80,40,0,0.28);margin-bottom:30px;}
.g17-t4-trans-btn{background:linear-gradient(135deg,#7a3800,#cc6600);border:none;color:#fff;font-size:17px;font-weight:900;padding:16px 50px;border-radius:28px;cursor:pointer;box-shadow:0 6px 28px rgba(180,80,0,0.55);transition:transform .15s;}
.g17-t4-trans-btn:active{transform:scale(.96);}
#g17S4{display:none;min-height:100vh;flex-direction:column;align-items:center;background:linear-gradient(170deg,#0a0300 0%,#190a01 55%,#0e0500 100%);padding-bottom:48px;direction:rtl;}
#g17S4.show{display:flex;}
.g17-s4-narration{font-size:13px;color:rgba(255,210,155,0.8);text-align:center;max-width:340px;line-height:1.75;padding:10px 20px 16px;border-bottom:1px solid rgba(200,130,0,0.22);margin-bottom:10px;width:100%;box-sizing:border-box;}
.g17-s4-task{font-size:12px;color:rgba(255,190,100,0.65);text-align:center;padding:0 20px 14px;direction:rtl;}
/* sortable cards */
.g17-s4-list{display:flex;flex-direction:column;gap:10px;width:100%;max-width:360px;padding:0 16px;box-sizing:border-box;margin-bottom:18px;}
.g17-s4-card{display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,rgba(60,25,0,0.7),rgba(40,15,0,0.85));border:2px solid rgba(200,130,0,0.35);border-radius:18px;padding:14px 18px;cursor:pointer;transition:transform .15s,background .2s,border-color .2s,box-shadow .2s;-webkit-tap-highlight-color:transparent;user-select:none;}
.g17-s4-card:hover{background:linear-gradient(135deg,rgba(90,40,0,0.75),rgba(60,25,0,0.9));}
.g17-s4-card.selected{border-color:#ffd700;background:linear-gradient(135deg,rgba(120,60,0,0.8),rgba(80,35,0,0.9));box-shadow:0 0 18px rgba(255,180,0,0.5);}
.g17-s4-card.correct-flash{border-color:#00e87a;box-shadow:0 0 18px rgba(0,220,120,0.5);}
.g17-s4-pos{font-size:13px;font-weight:900;color:rgba(200,140,60,0.7);min-width:20px;text-align:center;}
.g17-s4-emoji{font-size:36px;line-height:1;}
.g17-s4-label{font-size:16px;font-weight:800;color:rgba(255,220,160,0.95);flex:1;}
.g17-s4-drag-hint{font-size:11px;color:rgba(200,140,60,0.45);text-align:right;direction:rtl;}
/* hint for drag on desktop */
.g17-s4-info{font-size:12px;color:rgba(200,140,60,0.5);text-align:center;margin-bottom:10px;direction:rtl;}
/* check + feedback */
.g17-s4-check-btn{background:linear-gradient(135deg,#7a3800,#cc6600);border:none;color:#fff;font-size:15px;font-weight:900;padding:14px 36px;border-radius:16px;cursor:pointer;box-shadow:0 4px 18px rgba(160,70,0,0.4);transition:transform .12s;margin-bottom:10px;}
.g17-s4-check-btn:active{transform:scale(.95);}
.g17-s4-feedback{font-size:13px;font-weight:800;color:rgba(255,130,130,0.95);text-align:center;min-height:22px;direction:rtl;max-width:300px;padding:0 12px;}
.g17-s4-hint-box{font-size:13px;color:rgba(255,215,0,0.8);text-align:center;max-width:290px;padding:10px 16px;background:rgba(70,40,0,0.35);border:1px solid rgba(255,180,0,0.22);border-radius:12px;display:none;direction:rtl;line-height:1.6;margin-top:8px;}
/* success 4 */
#g17Success4{display:none;position:fixed;inset:0;background:rgba(5,2,0,0.92);z-index:220;flex-direction:column;align-items:center;justify-content:center;padding:32px 24px;text-align:center;direction:rtl;}
#g17Success4.show{display:flex;}
.g17-s4-orb{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff9e6,#ffb300,rgba(200,80,0,0));animation:g17orbpulse 1.6s ease-in-out infinite;margin-bottom:22px;display:flex;align-items:center;justify-content:center;font-size:52px;}
.g17-s4-success-hed{font-size:22px;font-weight:900;color:#ffcc44;margin-bottom:10px;text-shadow:0 0 20px rgba(255,180,0,0.6);}
.g17-s4-success-body{font-size:15px;color:rgba(255,230,180,0.9);line-height:1.8;max-width:300px;margin-bottom:28px;}
.g17-s4-continue-btn{background:linear-gradient(135deg,#7a3800,#cc6600);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(180,80,0,0.55);}
"""
if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_NEW, 1)
    print("CSS OK")
else:
    print("ERROR: CSS anchor not found")

# ─────────────────────────────────────────────────────────────────
# 2.  HTML (insert before closing </div> of game17UI)
# ─────────────────────────────────────────────────────────────────
HTML_ANCHOR = '    <button class="g17-s2-continue-btn" onclick="g17S2ContinueBtn()">המשך למסע 🌟</button>\n  </div>\n\n</div>\n\n<!-- ══ GAME 16'
HTML_NEW = '''    <button class="g17-s2-continue-btn" onclick="g17S2ContinueBtn()">המשך למסע 🌟</button>
  </div>

  <!-- ── TRANSITION → S4 ── -->
  <div id="g17Trans4">
    <div class="g17-t4-icon">⏳</div>
    <div class="g17-t4-trans-text">
      המראה נפתחה… ומאחוריה חדר שלא נראה כמוהו.<br><br>
      כאן הזמן שולט בכל. דברים נעלמים, משתנים, נשכחים.<br>
      אבל לא הכול נעלם באותו קצב.
    </div>
    <button class="g17-t4-trans-btn" onclick="g17EnterTimeRoom()">כניסה לחדר הזמן ⏳</button>
  </div>

  <!-- ── SCREEN 4 – TIME ROOM ── -->
  <div id="g17S4">
    <div class="g17-header">
      <button class="g17-back-btn" onclick="g17GoBack()">⬅ חזור</button>
      <div class="g17-screen-title">⏳ חדר הזמן</div>
      <div style="width:70px"></div>
    </div>
    <div class="g17-s4-narration">
      הכול משתנה עם הזמן.<br>אבל לא הכול נעלם באותו קצב.
    </div>
    <div class="g17-s4-task">סדר את הדברים לפי מה שנעלם ראשון ועד מה שנשאר אחרון.</div>
    <div class="g17-s4-info">לחץ על פריט → ואז על מיקום אחר להחלפה</div>

    <div class="g17-s4-list" id="g17S4List"></div>

    <button class="g17-s4-check-btn" onclick="g17CheckS4()">בדוק את הסדר ✓</button>
    <div class="g17-s4-feedback" id="g17S4Feedback"></div>
    <div class="g17-s4-hint-box" id="g17S4Hint">
      💡 חשוב מה קורה לכל אחד מהם עם הזמן — בטבע, בחיים, בלב.
    </div>
  </div>

  <!-- ── SUCCESS 4 ── -->
  <div id="g17Success4">
    <div class="g17-s4-orb">❤️</div>
    <div class="g17-s4-success-hed">הזמן הבין אותך.</div>
    <div class="g17-s4-success-body">
      הדרך נפתחת…<br>כי מה שנשאר בסוף הוא אהבה.
    </div>
    <button class="g17-s4-continue-btn" onclick="g17S4ContinueBtn()">המשך למסע 🌟</button>
  </div>

</div>

<!-- ══ GAME 16'''
if HTML_ANCHOR in content:
    content = content.replace(HTML_ANCHOR, HTML_NEW, 1)
    print("HTML OK")
else:
    print("ERROR: HTML anchor not found")
    idx = content.find('g17S2ContinueBtn()">המשך למסע')
    print(f"  button at idx: {idx}")

# ─────────────────────────────────────────────────────────────────
# 3.  JS – update g17S2ContinueBtn + add all S4 logic
# ─────────────────────────────────────────────────────────────────
OLD_JS = r"""function g17S2ContinueBtn() {
  // No screen 3 yet — close gracefully
  document.getElementById('g17Success2').classList.remove('show');
  g17GoBack();
}
</script>"""

NEW_JS = r"""function g17S2ContinueBtn() {
  document.getElementById('g17Success2').classList.remove('show');
  document.getElementById('g17S2').classList.remove('show');
  var t4 = document.getElementById('g17Trans4');
  if (t4) t4.classList.add('show');
}

/* ═══════════════════════════════════════════════
   SCREEN 4 – חדר הזמן (Time Room)
   ═══════════════════════════════════════════════ */
const G17_S4_ITEMS = [
  { id:'ice',    emoji:'🧊', label:'קרח'   },
  { id:'candle', emoji:'🕯️', label:'נר'    },
  { id:'rose',   emoji:'🌹', label:'ורד'   },
  { id:'love',   emoji:'❤️', label:'אהבה'  }
];
const G17_S4_CORRECT = ['ice','candle','rose','love'];
let g17S4Order = [];
let g17S4Selected = -1;
let g17S4WrongCount = 0;

function g17EnterTimeRoom() {
  var t4 = document.getElementById('g17Trans4');
  if (t4) t4.classList.remove('show');
  // shuffle order (make sure it's not already correct)
  g17S4Order = ['love','rose','ice','candle'];
  g17S4Selected = -1;
  g17S4WrongCount = 0;
  document.getElementById('g17S4Feedback').textContent = '';
  document.getElementById('g17S4Hint').style.display = 'none';
  document.getElementById('g17Success4').classList.remove('show');
  g17RenderS4();
  document.getElementById('g17S4').classList.add('show');
}

function g17RenderS4() {
  var list = document.getElementById('g17S4List');
  if (!list) return;
  var html = '';
  g17S4Order.forEach(function(id, i) {
    var item = G17_S4_ITEMS.find(function(x){ return x.id === id; });
    var sel = (i === g17S4Selected) ? ' selected' : '';
    var posLabels = ['ראשון','שני','שלישי','אחרון'];
    html += '<div class="g17-s4-card' + sel + '" onclick="g17S4Tap(' + i + ')" draggable="true" ondragstart="g17S4DragStart(event,' + i + ')" ondragover="g17S4DragOver(event)" ondrop="g17S4Drop(event,' + i + ')">'
          + '<div class="g17-s4-pos">' + (i+1) + '</div>'
          + '<div class="g17-s4-emoji">' + item.emoji + '</div>'
          + '<div class="g17-s4-label">' + item.label + '</div>'
          + '<div class="g17-s4-drag-hint">⠿</div>'
          + '</div>';
  });
  list.innerHTML = html;
}

/* tap-to-swap (works on all devices) */
function g17S4Tap(idx) {
  if (g17S4Selected === -1) {
    g17S4Selected = idx;
  } else if (g17S4Selected === idx) {
    g17S4Selected = -1;
  } else {
    var tmp = g17S4Order[g17S4Selected];
    g17S4Order[g17S4Selected] = g17S4Order[idx];
    g17S4Order[idx] = tmp;
    g17S4Selected = -1;
  }
  g17RenderS4();
}

/* drag-and-drop (desktop) */
var g17DragSrc = -1;
function g17S4DragStart(e, idx) {
  g17DragSrc = idx;
  e.dataTransfer.effectAllowed = 'move';
}
function g17S4DragOver(e) {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move';
}
function g17S4Drop(e, idx) {
  e.preventDefault();
  if (g17DragSrc < 0 || g17DragSrc === idx) { g17DragSrc = -1; return; }
  var tmp = g17S4Order[g17DragSrc];
  g17S4Order[g17DragSrc] = g17S4Order[idx];
  g17S4Order[idx] = tmp;
  g17DragSrc = -1;
  g17S4Selected = -1;
  g17RenderS4();
}

function g17CheckS4() {
  var match = G17_S4_CORRECT.every(function(id, i){ return g17S4Order[i] === id; });
  var fb = document.getElementById('g17S4Feedback');
  if (match) {
    g17S4Success();
  } else {
    g17S4WrongCount++;
    if (g17S4WrongCount >= 2) {
      document.getElementById('g17S4Hint').style.display = 'block';
    }
    fb.style.color = 'rgba(255,130,130,0.95)';
    fb.textContent = 'הזמן עדיין לא השתכנע… משהו כאן נעלם מוקדם מדי או מאוחר מדי.';
    // shake
    var cards = document.querySelectorAll('.g17-s4-card');
    cards.forEach(function(c){ c.style.animation='g17shake .35s ease'; });
    setTimeout(function(){ cards.forEach(function(c){ c.style.animation=''; }); fb.textContent=''; }, 1200);
  }
}

function g17S4Success() {
  document.getElementById('g17S4Feedback').textContent = '';
  document.getElementById('g17S4Hint').style.display = 'none';
  // flash cards green one by one
  var cards = document.querySelectorAll('.g17-s4-card');
  cards.forEach(function(c, i){
    setTimeout(function(){ c.classList.add('correct-flash'); }, i * 250);
  });
  setTimeout(function(){
    document.getElementById('g17Success4').classList.add('show');
  }, cards.length * 250 + 600);
}

function g17S4ContinueBtn() {
  document.getElementById('g17Success4').classList.remove('show');
  g17GoBack();
}
</script>"""

if OLD_JS in content:
    content = content.replace(OLD_JS, NEW_JS, 1)
    print("JS OK")
else:
    print("ERROR: JS anchor not found")
    idx = content.find('function g17S2ContinueBtn()')
    print(f"  g17S2ContinueBtn at: {idx}")

# ─────────────────────────────────────────────────────────────────
# 4.  Reset S4 screens on startGame17 re-entry
# ─────────────────────────────────────────────────────────────────
OLD_RESET = "  var g17s2ov = document.getElementById('g17Success2'); if(g17s2ov) g17s2ov.classList.remove('show');"
NEW_RESET = (OLD_RESET
  + "\n  var g17t4 = document.getElementById('g17Trans4'); if(g17t4) g17t4.classList.remove('show');"
  + "\n  var g17s4 = document.getElementById('g17S4'); if(g17s4) g17s4.classList.remove('show');"
  + "\n  var g17s4ov = document.getElementById('g17Success4'); if(g17s4ov) g17s4ov.classList.remove('show');")
if OLD_RESET in content:
    content = content.replace(OLD_RESET, NEW_RESET, 1)
    print("Reset OK")
else:
    print("WARN: reset anchor not found")

# ─────────────────────────────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done. {orig} → {len(content)} (+{len(content)-orig})")
