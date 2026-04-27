import re

filepath = '/sessions/bold-confident-feynman/mnt/outputs/כובש_השטחים.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

orig_len = len(content)
print(f"Original length: {orig_len}")

# ─────────────────────────────────────────
# 1. ADD CSS (after .gc-15:hover rule)
# ─────────────────────────────────────────
CSS_ANCHOR = '.gc-15:hover{box-shadow:0 8px 32px rgba(220,0,255,0.6);}'
CSS_INSERT = '''
/* ── Game 16 – מיקס מילים ── */
.gc-16{background:linear-gradient(145deg,#001a10,#004d2e);box-shadow:0 4px 22px rgba(0,220,120,0.22);}
.gc-16:hover{box-shadow:0 8px 32px rgba(0,255,140,0.5);}
#game16UI{display:none;position:fixed;inset:0;background:linear-gradient(160deg,#001a10 0%,#003322 50%,#001a10 100%);flex-direction:column;align-items:center;z-index:90;overflow-y:auto;padding:0 16px 40px;}
#game16UI.show{display:flex;}
.g16-header{width:100%;max-width:460px;display:flex;align-items:center;justify-content:space-between;padding:14px 0 10px;}
.g16-back{background:rgba(0,200,100,0.18);border:1.5px solid rgba(0,220,120,0.4);color:#7fffb8;font-size:14px;font-weight:800;padding:7px 14px;border-radius:12px;cursor:pointer;}
.g16-back:active{transform:scale(0.95);}
.g16-title{font-size:22px;font-weight:900;color:#fff;text-align:center;flex:1;direction:rtl;}
.g16-timer-wrap{width:100%;max-width:460px;display:flex;align-items:center;gap:12px;margin-bottom:14px;}
.g16-timer-bar-bg{flex:1;height:14px;background:rgba(255,255,255,0.1);border-radius:7px;overflow:hidden;}
.g16-timer-bar{height:100%;width:100%;background:linear-gradient(90deg,#00e87a,#00c46a);border-radius:7px;transition:width 0.25s linear,background 0.5s;}
.g16-timer-num{font-size:22px;font-weight:900;color:#00e87a;min-width:36px;text-align:center;}
.g16-score-row{display:flex;gap:20px;margin-bottom:18px;direction:rtl;}
.g16-score-box{background:rgba(0,200,100,0.12);border:1px solid rgba(0,200,100,0.3);border-radius:14px;padding:8px 20px;text-align:center;}
.g16-score-label{font-size:11px;color:rgba(0,220,120,0.7);font-weight:700;}
.g16-score-val{font-size:26px;font-weight:900;color:#00e87a;}
.g16-word-len{font-size:13px;color:rgba(200,255,230,0.6);margin-bottom:10px;direction:rtl;}
.g16-built-row{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;min-height:64px;align-items:center;margin-bottom:14px;direction:rtl;}
.g16-built-cell{width:52px;height:56px;background:rgba(0,160,80,0.25);border:2px solid rgba(0,220,120,0.5);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;color:#fff;cursor:pointer;transition:transform 0.1s,background 0.15s;}
.g16-built-cell.filled{background:rgba(0,180,90,0.45);border-color:rgba(0,255,140,0.8);}
.g16-built-cell.error{background:rgba(200,0,0,0.4);border-color:#ff4444;animation:g16shake 0.35s ease;}
.g16-built-cell.correct-flash{background:rgba(0,220,120,0.6);border-color:#00ffaa;}
@keyframes g16shake{0%{transform:translateX(0)}20%{transform:translateX(-6px)}40%{transform:translateX(6px)}60%{transform:translateX(-4px)}80%{transform:translateX(4px)}100%{transform:translateX(0)}}
.g16-letters-grid{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;max-width:420px;margin-bottom:18px;direction:rtl;}
.g16-letter-btn{width:58px;height:62px;background:linear-gradient(145deg,rgba(0,160,80,0.5),rgba(0,100,50,0.7));border:2px solid rgba(0,220,120,0.5);border-radius:14px;font-size:28px;font-weight:900;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform 0.1s,opacity 0.15s,background 0.15s;-webkit-tap-highlight-color:transparent;}
.g16-letter-btn:active{transform:scale(0.9);}
.g16-letter-btn.used{opacity:0.18;pointer-events:none;}
.g16-actions{display:flex;gap:12px;margin-bottom:20px;direction:rtl;}
.g16-act-btn{padding:10px 22px;border-radius:14px;font-size:14px;font-weight:800;cursor:pointer;border:none;transition:transform 0.1s,opacity 0.15s;}
.g16-act-btn:active{transform:scale(0.93);}
.g16-undo-btn{background:rgba(255,200,0,0.2);color:#ffd700;border:1.5px solid rgba(255,200,0,0.4);}
.g16-clear-btn{background:rgba(255,80,80,0.18);color:#ff8888;border:1.5px solid rgba(255,80,80,0.35);}
.g16-msg{font-size:17px;font-weight:800;color:#fff;min-height:28px;text-align:center;direction:rtl;transition:opacity 0.3s;}
.g16-confetti-wrap{position:fixed;inset:0;pointer-events:none;z-index:200;overflow:hidden;}
.g16-confetti-piece{position:absolute;width:10px;height:10px;border-radius:2px;animation:g16confFall linear forwards;}
@keyframes g16confFall{0%{transform:translateY(-20px) rotate(0deg);opacity:1}100%{transform:translateY(110vh) rotate(720deg);opacity:0}}
'''
if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_ANCHOR + CSS_INSERT, 1)
    print("CSS inserted OK")
else:
    print("ERROR: CSS anchor not found!")

# ─────────────────────────────────────────
# 2. ADD GAME CARD in עוד משחקים
# ─────────────────────────────────────────
CARD_ANCHOR = '''            <div class="game-card gc-9" onclick="startFromCard(9)">
              <div class="card-num-badge">14</div>
              <span class="card-icon">🥙</span>
              <div class="card-name">מלך הפלאפל</div>
              <div class="card-desc">תפוס פלאפלים לתוך הפיתה — היה המלך!</div>
            </div>
          </div>
        </div>'''
CARD_INSERT = '''            <div class="game-card gc-9" onclick="startFromCard(9)">
              <div class="card-num-badge">14</div>
              <span class="card-icon">🥙</span>
              <div class="card-name">מלך הפלאפל</div>
              <div class="card-desc">תפוס פלאפלים לתוך הפיתה — היה המלך!</div>
            </div>
            <div class="game-card gc-16" onclick="startFromCard(16)">
              <div class="card-num-badge">15</div>
              <span class="card-icon">🔤</span>
              <div class="card-name">מיקס מילים</div>
              <div class="card-desc">הרכב מילים מאותיות מבולבלות — תגבר על השעון!</div>
            </div>
          </div>
        </div>'''
if CARD_ANCHOR in content:
    content = content.replace(CARD_ANCHOR, CARD_INSERT, 1)
    print("Card inserted OK")
else:
    print("ERROR: Card anchor not found!")

# ─────────────────────────────────────────
# 3. ADD GAME HTML (before BREAK MODAL)
# ─────────────────────────────────────────
HTML_ANCHOR = '<!-- ══ BREAK MODAL ══ -->'
GAME_HTML = '''<!-- ══ GAME 16 – מיקס מילים ══ -->
<div id="game16UI">
  <div class="g16-header">
    <button class="g16-back" onclick="g16GoBack()">⬅ חזור</button>
    <div class="g16-title">🔤 מיקס מילים</div>
    <div style="width:70px"></div>
  </div>
  <div class="g16-score-row">
    <div class="g16-score-box"><div class="g16-score-label">ניקוד</div><div class="g16-score-val" id="g16Score">0</div></div>
    <div class="g16-score-box"><div class="g16-score-label">מילה</div><div class="g16-score-val" id="g16WordNum">1</div></div>
  </div>
  <div class="g16-timer-wrap">
    <div class="g16-timer-bar-bg"><div class="g16-timer-bar" id="g16TimerBar"></div></div>
    <div class="g16-timer-num" id="g16TimerNum">30</div>
  </div>
  <div class="g16-word-len" id="g16WordLen"></div>
  <div class="g16-built-row" id="g16BuiltRow"></div>
  <div class="g16-letters-grid" id="g16Letters"></div>
  <div class="g16-actions">
    <button class="g16-act-btn g16-undo-btn" onclick="g16UndoLast()">↩ בטל אחרון</button>
    <button class="g16-act-btn g16-clear-btn" onclick="g16Clear()">🗑 נקה הכל</button>
  </div>
  <div class="g16-msg" id="g16Msg"></div>
  <div class="g16-confetti-wrap" id="g16ConfWrap"></div>
</div>

<!-- ══ BREAK MODAL ══ -->'''
if HTML_ANCHOR in content:
    content = content.replace(HTML_ANCHOR, GAME_HTML, 1)
    print("HTML inserted OK")
else:
    print("ERROR: HTML anchor not found!")

# ─────────────────────────────────────────
# 4. ADD ROUTING in startFromCard
# ─────────────────────────────────────────
ROUTE_ANCHOR = '  if(lvl===15){startGame15();return;}'
ROUTE_INSERT = '  if(lvl===15){startGame15();return;}\n  if(lvl===16){startGame16();return;}'
if ROUTE_ANCHOR in content:
    content = content.replace(ROUTE_ANCHOR, ROUTE_INSERT, 1)
    print("Route inserted OK")
else:
    print("ERROR: Route anchor not found!")

# ─────────────────────────────────────────
# 5. ADD CLEANUP in hideGame
# ─────────────────────────────────────────
HIDE_ANCHOR = '  g15ExitToMenu&&g15ExitToMenu(true);'
HIDE_INSERT = '  g15ExitToMenu&&g15ExitToMenu(true);\n  g16ExitToMenu&&g16ExitToMenu(true);'
if HIDE_ANCHOR in content:
    content = content.replace(HIDE_ANCHOR, HIDE_INSERT, 1)
    print("Hide cleanup inserted OK")
else:
    print("ERROR: Hide anchor not found!")

# ─────────────────────────────────────────
# 6. ADD JS (before closing </script>)
# ─────────────────────────────────────────
JS_ANCHOR = '</script>\n</body>'
GAME_JS = r"""
/* ═══════════════════════════════════════════════
   GAME 16 – מיקס מילים (Word Scramble)
   ═══════════════════════════════════════════════ */
const G16_WORDS = [
  'מחשבון','מחברות','מצלמות','ספריות','חשמלית','תחבורה',
  'מערכות','תהליכים','החלטות','הצלחות','כישלונות','שינויים',
  'סקרנות','תקשורת','הקשבה','חיבורים','אמונות','ביטחון',
  'יציבות','רגישות','חברויות','אהבות','התלהבות','התרגשות',
  'התקדמות','התמודדות','התחדשות','מחשבות','גלריות','מוזיקה',
  'מסעדות','חקירות','גילויים','שלווה','תשוקה','תעשייה',
  'מזרקות','תחושות','הזדמנות','גלריה','מסעדה','חקירה',
  'השראה','ידידות','משפחה','אומץ','חכמה','צדקה','שמחה',
  'הרפתקה','יצירתיות','עצמאות','מנהיגות','כבוד','אמנות'
];
const G16_TIME = 30;
let g16State = {
  score: 0, wordNum: 0, word: '', scrambled: [],
  built: [], usedIdx: [], timerSec: G16_TIME,
  timerRaf: null, timerStart: null, running: false,
  usedWords: []
};
let g16ExitToMenu = null;

function startGame16() {
  if (g16ExitToMenu) g16ExitToMenu(false);
  var ui = document.getElementById('game16UI');
  g16State.score = 0;
  g16State.wordNum = 0;
  g16State.usedWords = [];
  g16UpdateScore();
  g16ExitToMenu = function(silent) {
    g16StopTimer();
    g16ExitToMenu = null;
    if (!silent) { hideGame(); navTo('mainPage'); }
  };
  ui.classList.add('show');
  navTo('game16UI');
  g16NewRound();
}

function g16GoBack() {
  if (g16ExitToMenu) g16ExitToMenu(false);
  else { hideGame(); navTo('mainPage'); }
}

function g16NewRound() {
  g16StopTimer();
  // pick unused word
  var pool = G16_WORDS.filter(function(w){ return g16State.usedWords.indexOf(w) === -1; });
  if (pool.length === 0) { g16State.usedWords = []; pool = G16_WORDS.slice(); }
  var word = pool[Math.floor(Math.random() * pool.length)];
  g16State.usedWords.push(word);
  g16State.word = word;
  g16State.wordNum++;
  // scramble — ensure different from original
  var letters = word.split('');
  var scrambled;
  var tries = 0;
  do {
    scrambled = letters.slice().sort(function(){ return Math.random()-0.5; });
    tries++;
  } while (scrambled.join('') === word && tries < 20);
  g16State.scrambled = scrambled;
  g16State.built = [];
  g16State.usedIdx = [];
  g16State.running = true;
  g16State.timerSec = G16_TIME;
  document.getElementById('g16WordNum').textContent = g16State.wordNum;
  document.getElementById('g16WordLen').textContent = 'מילה בת ' + word.length + ' אותיות';
  document.getElementById('g16Msg').textContent = '';
  g16RenderBuilt();
  g16RenderLetters();
  g16StartTimer();
}

function g16RenderBuilt() {
  var row = document.getElementById('g16BuiltRow');
  var word = g16State.word;
  var html = '';
  for (var i = 0; i < word.length; i++) {
    var letter = g16State.built[i] || '';
    var cls = 'g16-built-cell' + (letter ? ' filled' : '');
    html += '<div class="' + cls + '" data-pos="' + i + '">' + letter + '</div>';
  }
  row.innerHTML = html;
}

function g16RenderLetters() {
  var grid = document.getElementById('g16Letters');
  var html = '';
  g16State.scrambled.forEach(function(ch, i) {
    var used = g16State.usedIdx.indexOf(i) !== -1;
    html += '<button class="g16-letter-btn' + (used ? ' used' : '') + '" onclick="g16ClickLetter(' + i + ')">' + ch + '</button>';
  });
  grid.innerHTML = html;
}

function g16ClickLetter(idx) {
  if (!g16State.running) return;
  if (g16State.usedIdx.indexOf(idx) !== -1) return;
  if (g16State.built.length >= g16State.word.length) return;
  g16State.built.push(g16State.scrambled[idx]);
  g16State.usedIdx.push(idx);
  g16RenderBuilt();
  g16RenderLetters();
  if (g16State.built.length === g16State.word.length) {
    setTimeout(g16CheckWord, 80);
  }
}

function g16UndoLast() {
  if (!g16State.running) return;
  if (g16State.built.length === 0) return;
  g16State.built.pop();
  g16State.usedIdx.pop();
  g16RenderBuilt();
  g16RenderLetters();
}

function g16Clear() {
  if (!g16State.running) return;
  g16State.built = [];
  g16State.usedIdx = [];
  g16RenderBuilt();
  g16RenderLetters();
}

function g16CheckWord() {
  var attempt = g16State.built.join('');
  if (attempt === g16State.word) {
    g16ShowSuccess();
  } else {
    g16ShowError();
  }
}

function g16ShowSuccess() {
  g16StopTimer();
  g16State.running = false;
  var speedBonus = Math.round(g16State.timerSec * 0.5);
  var pts = 10 + speedBonus;
  g16State.score += pts;
  g16UpdateScore();
  // flash cells green
  var cells = document.querySelectorAll('.g16-built-cell');
  cells.forEach(function(c){ c.classList.add('correct-flash'); });
  document.getElementById('g16Msg').textContent = '✅ נכון! +' + pts + ' נקודות 🎉';
  g16Confetti();
  setTimeout(g16NewRound, 1800);
}

function g16ShowError() {
  // shake built row
  var cells = document.querySelectorAll('.g16-built-cell');
  cells.forEach(function(c){ c.classList.add('error'); });
  setTimeout(function(){
    cells.forEach(function(c){ c.classList.remove('error'); });
  }, 400);
  // clear and let try again
  g16State.built = [];
  g16State.usedIdx = [];
  setTimeout(function(){
    g16RenderBuilt();
    g16RenderLetters();
    document.getElementById('g16Msg').textContent = '❌ לא נכון, נסה שוב!';
    setTimeout(function(){ document.getElementById('g16Msg').textContent = ''; }, 1200);
  }, 400);
}

function g16TimeUp() {
  g16State.running = false;
  document.getElementById('g16Msg').textContent = '⏰ הזמן נגמר! המילה: ' + g16State.word;
  // show answer in built row
  g16State.built = g16State.word.split('');
  g16RenderBuilt();
  var btns = document.querySelectorAll('.g16-letter-btn');
  btns.forEach(function(b){ b.classList.add('used'); });
  setTimeout(g16NewRound, 2200);
}

function g16StartTimer() {
  g16State.timerStart = performance.now();
  var totalMs = G16_TIME * 1000;
  function tick(now) {
    var elapsed = now - g16State.timerStart;
    var remaining = Math.max(0, totalMs - elapsed);
    var secs = Math.ceil(remaining / 1000);
    if (secs !== g16State.timerSec) {
      g16State.timerSec = secs;
      document.getElementById('g16TimerNum').textContent = secs;
    }
    var pct = remaining / totalMs * 100;
    var bar = document.getElementById('g16TimerBar');
    if (bar) {
      bar.style.width = pct + '%';
      if (pct < 30) { bar.style.background = 'linear-gradient(90deg,#ff4444,#cc2222)'; }
      else if (pct < 60) { bar.style.background = 'linear-gradient(90deg,#ffaa00,#cc8800)'; }
      else { bar.style.background = 'linear-gradient(90deg,#00e87a,#00c46a)'; }
    }
    if (remaining <= 0) { g16TimeUp(); return; }
    g16State.timerRaf = requestAnimationFrame(tick);
  }
  g16State.timerRaf = requestAnimationFrame(tick);
}

function g16StopTimer() {
  if (g16State.timerRaf) { cancelAnimationFrame(g16State.timerRaf); g16State.timerRaf = null; }
}

function g16UpdateScore() {
  var el = document.getElementById('g16Score');
  if (el) el.textContent = g16State.score;
}

function g16Confetti() {
  var wrap = document.getElementById('g16ConfWrap');
  if (!wrap) return;
  wrap.innerHTML = '';
  var colors = ['#00e87a','#ffd700','#ff6b6b','#7ec8e3','#ff80c8','#fff'];
  for (var i = 0; i < 48; i++) {
    var p = document.createElement('div');
    p.className = 'g16-confetti-piece';
    p.style.left = (Math.random() * 100) + '%';
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.width = (8 + Math.random() * 10) + 'px';
    p.style.height = (8 + Math.random() * 10) + 'px';
    p.style.animationDuration = (1.2 + Math.random() * 1.4) + 's';
    p.style.animationDelay = (Math.random() * 0.4) + 's';
    wrap.appendChild(p);
    setTimeout(function(el){ el.remove(); }, 3000, p);
  }
}
"""
if JS_ANCHOR in content:
    content = content.replace(JS_ANCHOR, GAME_JS + JS_ANCHOR, 1)
    print("JS inserted OK")
else:
    print("ERROR: JS anchor not found!")

# ─────────────────────────────────────────
# WRITE BACK
# ─────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
new_len = len(content)
print(f"New length: {new_len}  (diff: +{new_len - orig_len})")
