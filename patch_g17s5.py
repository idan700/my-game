# -*- coding: utf-8 -*-
filepath = '/sessions/bold-confident-feynman/mnt/outputs/כובש_השטחים.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
orig = len(content)
print(f"Original: {orig}")

# ─────────────────────────────────────────────────────────────────
# 1.  CSS
# ─────────────────────────────────────────────────────────────────
CSS_ANCHOR = '.g17-s4-continue-btn{background:linear-gradient(135deg,#7a3800,#cc6600);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(180,80,0,0.55);}'
CSS_NEW = CSS_ANCHOR + r"""
/* ══════ SCREEN 5 – CALENDAR ROOM ══════ */
#g17Trans5{display:none;min-height:100vh;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(170deg,#010510 0%,#040d28 55%,#020818 100%);padding:40px 28px;text-align:center;direction:rtl;}
#g17Trans5.show{display:flex;}
.g17-t5-icon{font-size:60px;margin-bottom:20px;animation:g17transFloat 3s ease-in-out infinite;}
.g17-t5-trans-text{font-size:15px;color:rgba(160,190,255,0.88);line-height:1.85;max-width:320px;border:1px solid rgba(80,120,255,0.25);border-radius:18px;padding:20px 22px;background:rgba(10,20,80,0.3);margin-bottom:30px;}
.g17-t5-trans-btn{background:linear-gradient(135deg,#0a2080,#1a4acc);border:none;color:#fff;font-size:17px;font-weight:900;padding:16px 50px;border-radius:28px;cursor:pointer;box-shadow:0 6px 28px rgba(30,80,220,0.55);transition:transform .15s;}
.g17-t5-trans-btn:active{transform:scale(.96);}
#g17S5{display:none;min-height:100vh;flex-direction:column;align-items:center;background:linear-gradient(170deg,#010510 0%,#030d25 55%,#020818 100%);padding-bottom:48px;direction:rtl;}
#g17S5.show{display:flex;}
.g17-s5-narration{font-size:13px;color:rgba(160,190,255,0.82);text-align:center;max-width:340px;line-height:1.75;padding:10px 20px 14px;border-bottom:1px solid rgba(80,120,255,0.2);margin-bottom:14px;width:100%;box-sizing:border-box;}
/* clue notes */
.g17-clues-wrap{display:flex;flex-direction:column;gap:10px;width:100%;max-width:400px;padding:0 14px;box-sizing:border-box;margin-bottom:16px;}
.g17-clue-note{background:rgba(255,255,255,0.04);border:1px solid rgba(100,140,255,0.3);border-radius:14px;padding:12px 16px;direction:rtl;}
.g17-clue-title{font-size:11px;color:rgba(140,170,255,0.6);font-weight:800;letter-spacing:1.5px;margin-bottom:8px;}
.g17-clue-seq{display:flex;gap:6px;align-items:flex-end;flex-wrap:wrap;direction:rtl;}
.g17-clue-letter{display:flex;flex-direction:column;align-items:center;gap:2px;}
.g17-clue-heart{font-size:14px;line-height:1;color:#ff4080;visibility:hidden;}
.g17-clue-heart.show{visibility:visible;}
.g17-clue-char{font-size:15px;font-weight:900;color:rgba(200,215,255,0.9);width:20px;text-align:center;}
.g17-clue-char.active{color:#ffd700;text-shadow:0 0 8px rgba(255,215,0,0.7);}
.g17-clue-year-wrap{display:flex;align-items:center;gap:12px;justify-content:center;margin-top:4px;}
.g17-clue-box{width:44px;height:44px;border:2px solid rgba(100,140,255,0.6);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:900;color:#ffd700;box-shadow:0 0 12px rgba(100,140,255,0.3);}
.g17-clue-eq{font-size:16px;color:rgba(160,190,255,0.75);font-weight:700;}
.g17-clue-result{font-size:20px;font-weight:900;color:rgba(140,180,255,0.9);}
/* calendar */
.g17-cal-wrap{width:100%;max-width:360px;padding:0 14px;box-sizing:border-box;margin-bottom:16px;}
.g17-cal-month{font-size:13px;font-weight:900;color:#7aa8ff;text-align:center;letter-spacing:2px;margin-bottom:8px;direction:rtl;}
.g17-cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;}
.g17-cal-hdr{font-size:11px;font-weight:900;color:rgba(140,170,255,0.55);text-align:center;padding:4px 2px;}
.g17-cal-hdr.thu{color:rgba(255,215,0,0.75);}
.g17-cal-day{font-size:13px;font-weight:700;color:rgba(180,205,255,0.65);text-align:center;padding:5px 2px;border-radius:6px;cursor:pointer;transition:background .15s,color .15s;}
.g17-cal-day:hover{background:rgba(80,120,255,0.2);}
.g17-cal-day.empty{cursor:default;}
.g17-cal-day.thu{color:rgba(255,215,0,0.8);}
.g17-cal-day.selected{background:rgba(255,215,0,0.25);color:#ffd700;font-weight:900;box-shadow:0 0 10px rgba(255,215,0,0.4);}
.g17-cal-day.target-thu{background:rgba(255,100,180,0.15);border:1px solid rgba(255,100,180,0.35);color:#ff80c8;}
/* code input */
.g17-s5-lock-wrap{display:flex;flex-direction:column;align-items:center;gap:10px;padding:0 16px;width:100%;max-width:380px;box-sizing:border-box;}
.g17-s5-label{font-size:12px;color:rgba(140,170,255,0.6);font-weight:800;letter-spacing:1px;direction:rtl;}
.g17-s5-code-row{display:flex;gap:10px;align-items:center;direction:ltr;}
.g17-s5-input{width:150px;height:52px;background:rgba(2,5,20,0.9);border:2px solid rgba(80,120,255,0.7);border-radius:14px;color:#ffd700;font-size:22px;font-weight:900;text-align:center;letter-spacing:4px;outline:none;caret-color:#ffd700;transition:border-color .2s,box-shadow .2s;}
.g17-s5-input:focus{border-color:#6699ff;box-shadow:0 0 18px rgba(80,140,255,0.45);}
.g17-s5-open-btn{background:linear-gradient(135deg,#0a2080,#1a4acc);border:none;color:#fff;font-size:14px;font-weight:900;padding:14px 18px;border-radius:14px;cursor:pointer;box-shadow:0 4px 16px rgba(30,80,220,0.4);transition:transform .12s;}
.g17-s5-open-btn:active{transform:scale(.95);}
.g17-s5-feedback{font-size:13px;font-weight:800;color:rgba(255,130,130,0.95);text-align:center;min-height:22px;direction:rtl;}
.g17-s5-hint{font-size:13px;color:rgba(255,215,0,0.8);text-align:center;max-width:290px;padding:10px 16px;background:rgba(40,50,0,0.35);border:1px solid rgba(255,200,0,0.22);border-radius:12px;display:none;direction:rtl;line-height:1.6;margin-top:6px;}
/* success 5 */
#g17Success5{display:none;position:fixed;inset:0;background:rgba(0,2,12,0.93);z-index:220;flex-direction:column;align-items:center;justify-content:center;padding:32px 24px;text-align:center;direction:rtl;}
#g17Success5.show{display:flex;}
.g17-s5-orb{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#d0e8ff,#4488ff,rgba(20,60,200,0));animation:g17orbpulse 1.6s ease-in-out infinite;margin-bottom:22px;display:flex;align-items:center;justify-content:center;font-size:52px;}
.g17-s5-success-hed{font-size:21px;font-weight:900;color:#88bbff;margin-bottom:10px;text-shadow:0 0 20px rgba(80,140,255,0.6);}
.g17-s5-success-body{font-size:15px;color:rgba(180,210,255,0.9);line-height:1.8;max-width:300px;margin-bottom:28px;}
.g17-s5-continue-btn{background:linear-gradient(135deg,#0a2080,#1a4acc);border:none;color:#fff;font-size:16px;font-weight:900;padding:16px 48px;border-radius:26px;cursor:pointer;box-shadow:0 6px 28px rgba(30,80,220,0.55);}
"""
if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_NEW, 1)
    print("CSS OK")
else:
    print("ERROR: CSS anchor not found")

# ─────────────────────────────────────────────────────────────────
# 2.  HTML
# ─────────────────────────────────────────────────────────────────
HTML_ANCHOR = '    <button class="g17-s4-continue-btn" onclick="g17S4ContinueBtn()">המשך למסע 🌟</button>\n  </div>\n\n</div>\n\n<!-- ══ GAME 16'
HTML_NEW = '''    <button class="g17-s4-continue-btn" onclick="g17S4ContinueBtn()">המשך למסע 🌟</button>
  </div>

  <!-- ── TRANSITION → S5 ── -->
  <div id="g17Trans5">
    <div class="g17-t5-icon">📅</div>
    <div class="g17-t5-trans-text">
      הזמן לא עוצר… אבל הוא גם לא מתגלה למי שלא יודע לקרוא אותו.<br><br>
      רגע אחד נכון — יכול לפתוח דרך שלמה.
    </div>
    <button class="g17-t5-trans-btn" onclick="g17EnterCalRoom()">כניסה לחדר הזמן 📅</button>
  </div>

  <!-- ── SCREEN 5 – CALENDAR ROOM ── -->
  <div id="g17S5">
    <div class="g17-header">
      <button class="g17-back-btn" onclick="g17GoBack()">⬅ חזור</button>
      <div class="g17-screen-title">📅 חדר הזמן</div>
      <div style="width:70px"></div>
    </div>
    <div class="g17-s5-narration">
      הזמן מפוזר סביבך.<br>
      אבל רק סדר נכון — יחשוף את הרגע.
    </div>

    <div class="g17-clues-wrap">

      <!-- Clue 1: Days of week -->
      <div class="g17-clue-note">
        <div class="g17-clue-title">🔹 רמז א׳ — ימי השבוע</div>
        <div class="g17-clue-seq" id="g17Clue1"></div>
      </div>

      <!-- Clue 2: Months -->
      <div class="g17-clue-note">
        <div class="g17-clue-title">🔹 רמז ב׳ — החודשים</div>
        <div class="g17-clue-seq" id="g17Clue2"></div>
      </div>

      <!-- Clue 3: Year -->
      <div class="g17-clue-note">
        <div class="g17-clue-title">🔹 רמז ג׳ — השנה</div>
        <div class="g17-clue-year-wrap">
          <div class="g17-clue-box">9</div>
          <div class="g17-clue-eq">² = 81</div>
          <div class="g17-clue-eq">→</div>
          <div class="g17-clue-result">שנה: <strong>81</strong></div>
        </div>
      </div>

    </div>

    <!-- Calendar -->
    <div class="g17-cal-wrap">
      <div class="g17-cal-month">✦ מאי ✦</div>
      <div class="g17-cal-grid" id="g17CalGrid"></div>
    </div>

    <!-- Code input -->
    <div class="g17-s5-lock-wrap">
      <div class="g17-s5-label">הקלד את הרגע המדויק (יום + חודש + שנה)</div>
      <div class="g17-s5-code-row">
        <input class="g17-s5-input" id="g17S5Code" type="tel" maxlength="6" placeholder="??????"/>
        <button class="g17-s5-open-btn" onclick="g17CheckS5()">פתח 🔑</button>
      </div>
      <div class="g17-s5-feedback" id="g17S5Feedback"></div>
      <div class="g17-s5-hint" id="g17S5Hint">
        💡 זה לא רק תאריך. זה רגע שלם.
      </div>
    </div>
  </div>

  <!-- ── SUCCESS 5 ── -->
  <div id="g17Success5">
    <div class="g17-s5-orb">📅</div>
    <div class="g17-s5-success-hed">אתה לא רק מצאת את היום —</div>
    <div class="g17-s5-success-body">
      אתה הבנת את הזמן.
    </div>
    <button class="g17-s5-continue-btn" onclick="g17S5ContinueBtn()">המשך למסע 🌟</button>
  </div>

</div>

<!-- ══ GAME 16'''
if HTML_ANCHOR in content:
    content = content.replace(HTML_ANCHOR, HTML_NEW, 1)
    print("HTML OK")
else:
    print("ERROR: HTML anchor not found")

# ─────────────────────────────────────────────────────────────────
# 3.  JS
# ─────────────────────────────────────────────────────────────────
OLD_JS = r"""function g17S4ContinueBtn() {
  document.getElementById('g17Success4').classList.remove('show');
  g17GoBack();
}
</script>"""

NEW_JS = r"""function g17S4ContinueBtn() {
  document.getElementById('g17Success4').classList.remove('show');
  document.getElementById('g17S4').classList.remove('show');
  var t5 = document.getElementById('g17Trans5');
  if (t5) t5.classList.add('show');
}

/* ═══════════════════════════════════════════════
   SCREEN 5 – חדר הזמן (Calendar Room)
   ═══════════════════════════════════════════════ */
const G17_S5_CODE = '190581';
let g17S5WrongCount = 0;
let g17S5SelDay = null;

function g17EnterCalRoom() {
  var t5 = document.getElementById('g17Trans5');
  if (t5) t5.classList.remove('show');
  g17S5WrongCount = 0;
  g17S5SelDay = null;
  document.getElementById('g17S5Code').value = '';
  document.getElementById('g17S5Feedback').textContent = '';
  document.getElementById('g17S5Hint').style.display = 'none';
  document.getElementById('g17Success5').classList.remove('show');
  g17BuildClue1();
  g17BuildClue2();
  g17BuildCalendar();
  document.getElementById('g17S5').classList.add('show');
}

function g17BuildClue1() {
  // ר,ש,ש,ר,ח,ש,ש  — heart above position 4 (ח)
  var seq = ['ר','ש','ש','ר','ח','ש','ש'];
  var heartIdx = 4; // 0-based: ח is index 4
  var wrap = document.getElementById('g17Clue1');
  if (!wrap) return;
  var html = '';
  seq.forEach(function(ch, i) {
    var active = i === heartIdx ? ' active' : '';
    var heartShow = i === heartIdx ? ' show' : '';
    html += '<div class="g17-clue-letter">'
          + '<div class="g17-clue-heart' + heartShow + '">❤️</div>'
          + '<div class="g17-clue-char' + active + '">' + ch + '</div>'
          + '</div>';
  });
  wrap.innerHTML = html;
}

function g17BuildClue2() {
  // י,פ,מ,א,מ,י,י,א,ס,א,נ,ד — heart above position 4 (מ = מאי)
  var seq = ['י','פ','מ','א','מ','י','י','א','ס','א','נ','ד'];
  var heartIdx = 4; // מ at index 4 = May
  var wrap = document.getElementById('g17Clue2');
  if (!wrap) return;
  var html = '';
  seq.forEach(function(ch, i) {
    var active = i === heartIdx ? ' active' : '';
    var heartShow = i === heartIdx ? ' show' : '';
    html += '<div class="g17-clue-letter">'
          + '<div class="g17-clue-heart' + heartShow + '">❤️</div>'
          + '<div class="g17-clue-char' + active + '">' + ch + '</div>'
          + '</div>';
  });
  wrap.innerHTML = html;
}

function g17BuildCalendar() {
  var grid = document.getElementById('g17CalGrid');
  if (!grid) return;
  // Headers: Sun(ר)=1, Mon(ש)=2, Tue(ש)=3, Wed(ר)=4, Thu(ח)=5, Fri(ש)=6, Sat(ש)=7
  var hdrs = ['ר','ש','ש','ר','ח','ש','ש'];
  var html = '';
  hdrs.forEach(function(h, i) {
    var cls = i === 4 ? ' thu' : ''; // index 4 = Thursday col
    html += '<div class="g17-cal-hdr' + cls + '">' + h + '</div>';
  });
  // May starts Sunday (index 0), 31 days
  // Thursdays: 5,12,19,26 → 3rd Thursday = 19
  var thuDays = [5,12,19,26];
  var target = 19;
  var startDay = 0; // Sunday = index 0
  // empty cells before day 1
  for (var e = 0; e < startDay; e++) {
    html += '<div class="g17-cal-day empty"></div>';
  }
  for (var d = 1; d <= 31; d++) {
    var col = (startDay + d - 1) % 7;
    var isThu = (col === 4);
    var isTarget = (d === target);
    var cls = '';
    if (isThu) cls += ' thu';
    if (isTarget) cls += ' target-thu';
    html += '<div class="g17-cal-day' + cls + '" onclick="g17CalTap(' + d + ')">' + d + '</div>';
  }
  grid.innerHTML = html;
}

function g17CalTap(day) {
  // highlight tapped day
  g17S5SelDay = day;
  var days = document.querySelectorAll('.g17-cal-day:not(.empty)');
  days.forEach(function(el){ el.classList.remove('selected'); });
  // find and mark
  days.forEach(function(el){
    if (parseInt(el.textContent) === day) el.classList.add('selected');
  });
  // auto-fill day portion if not already entered
  var inp = document.getElementById('g17S5Code');
  var dayStr = day < 10 ? '0'+day : ''+day;
  if (inp.value.length < 2) { inp.value = dayStr; }
}

function g17CheckS5() {
  var val = document.getElementById('g17S5Code').value.trim();
  var fb = document.getElementById('g17S5Feedback');
  if (val.length < 6) {
    fb.style.color = 'rgba(255,200,100,0.9)';
    fb.textContent = 'הקוד צריך להיות 6 ספרות (יום + חודש + שנה).';
    return;
  }
  if (val === G17_S5_CODE) {
    g17S5Success();
  } else {
    g17S5WrongCount++;
    if (g17S5WrongCount >= 2) {
      document.getElementById('g17S5Hint').style.display = 'block';
    }
    fb.style.color = 'rgba(255,130,130,0.95)';
    fb.textContent = 'הזמן זז… אבל לא עצרת ברגע הנכון.';
    var inp = document.getElementById('g17S5Code');
    inp.style.borderColor = '#ff4444';
    setTimeout(function(){ inp.style.borderColor = ''; fb.textContent = ''; }, 1000);
    document.getElementById('g17S5Code').value = '';
  }
}

function g17S5Success() {
  document.getElementById('g17S5Feedback').textContent = '';
  document.getElementById('g17S5Hint').style.display = 'none';
  // flash calendar target day
  var days = document.querySelectorAll('.g17-cal-day.target-thu');
  days.forEach(function(el){ el.classList.add('selected'); });
  setTimeout(function(){
    document.getElementById('g17Success5').classList.add('show');
  }, 800);
}

function g17S5ContinueBtn() {
  document.getElementById('g17Success5').classList.remove('show');
  g17GoBack();
}
</script>"""

if OLD_JS in content:
    content = content.replace(OLD_JS, NEW_JS, 1)
    print("JS OK")
else:
    print("ERROR: JS anchor not found")
    idx = content.find('function g17S4ContinueBtn()')
    print(f"  found at: {idx}")

# ─────────────────────────────────────────────────────────────────
# 4. Reset on startGame17
# ─────────────────────────────────────────────────────────────────
OLD_R = "  var g17s4ov = document.getElementById('g17Success4'); if(g17s4ov) g17s4ov.classList.remove('show');"
NEW_R = (OLD_R
  + "\n  var g17t5=document.getElementById('g17Trans5');if(g17t5)g17t5.classList.remove('show');"
  + "\n  var g17s5=document.getElementById('g17S5');if(g17s5)g17s5.classList.remove('show');"
  + "\n  var g17s5ov=document.getElementById('g17Success5');if(g17s5ov)g17s5ov.classList.remove('show');")
if OLD_R in content:
    content = content.replace(OLD_R, NEW_R, 1)
    print("Reset OK")
else:
    print("WARN: reset anchor not found")

# ─────────────────────────────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done. {orig} → {len(content)} (+{len(content)-orig})")
