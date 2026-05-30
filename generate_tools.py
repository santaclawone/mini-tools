#!/usr/bin/env python3
"""Generate all 18 mini tool HTML pages with ceramic glossy design."""

import os

BASE = r"C:\Users\openclaw_AI\.openclaw\workspace\developer\mini-tools\tools"

# Shared cursor/font loader JS snippet (minified)
CURSOR_JS = '''(function(){var g=document.getElementById("cursor-glow"),d=document.getElementById("cursor-dot");if(!g||!d)return;if("ontouchstart"in window||navigator.maxTouchPoints>0){g.style.display="none";d.style.display="none";return}var mx=-100,my=-100,gx=-100,gy=-100;document.addEventListener("mousemove",function(e){mx=e.clientX;my=e.clientY;d.style.left=mx+"px";d.style.top=my+"px"});!function a(){gx+=(mx-gx)*.12;gy+=(my-gy)*.12;g.style.left=gx+"px";g.style.top=gy+"px";requestAnimationFrame(a)}();document.querySelectorAll("a,button,.btn,input,textarea,select,.sample-btn,.chip,.quick-fill button,.choice-btn").forEach(function(e){e.addEventListener("mouseenter",function(){g.style.width="48px";g.style.height="48px"});e.addEventListener("mouseleave",function(){g.style.width="32px";g.style.height="32px"})});document.addEventListener("mousedown",function(){d.style.width="4px";d.style.height="4px"});document.addEventListener("mouseup",function(){d.style.width="6px";d.style.height="6px"})})();'''

HEADER = '''<header class="site-header">
  <div class="container">
    <div><div class="site-title">mini<span>tools</span></div><div class="site-subtitle">extracted from conversations</div></div>
    <nav class="site-nav"><a href="../../">home</a><a href="https://github.com/santaclawone">source</a></nav>
  </div>
</header>'''

FOOTER = '''<footer class="site-footer"><div class="container">Built from podcast conversations. No fluff.</div></footer>'''

def base_html(title, desc, badge, h1_text, body_html, extra_style="", extra_js=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../style.css">
<style>
.result-section {{ margin-bottom: var(--space-md); animation: fadeSlideIn 0.4s ease both; }}
.result-section h4 {{ font-size: 0.7rem; font-family: var(--font-heading); text-transform: uppercase; letter-spacing: 0.15em; color: var(--amber); margin-bottom: 0.5rem; opacity: 0.8; }}
.result-section ul {{ list-style: none; padding: 0; }}
.result-section li {{ padding: 0.3rem 0; font-size: 0.82rem; color: var(--text-secondary); border-bottom: 1px solid var(--border); }}
.highlight-block {{ background: rgba(15,23,42,0.5); border-left: 2px solid var(--amber); padding: var(--space-xs) var(--space-sm); margin: var(--space-xs) 0; font-size: 0.8rem; color: var(--text-secondary); line-height: 1.7; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }}
.metric-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-xs); margin: var(--space-sm) 0; }}
.metric-box {{ background: rgba(15,23,42,0.5); padding: var(--space-sm); border: 1px solid var(--border); border-radius: var(--radius-sm); text-align: center; }}
.metric-box strong {{ display: block; font-size: 1.5rem; font-weight: 700; font-family: var(--font-heading); color: var(--amber); }}
.metric-box span {{ font-size: 0.6rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.12em; margin-top: 0.2rem; display: block; }}
.choice-btn {{ padding: 0.4rem 0.8rem; background: transparent; border: 1px solid var(--border); border-radius: var(--radius-sm); color: var(--text-secondary); cursor: pointer; transition: all 0.2s; font-size: 0.8rem; font-family: var(--font-body); }}
.choice-btn:hover {{ border-color: var(--amber); color: var(--amber); background: rgba(245,158,11,0.04); }}
.choice-btn.active {{ border-color: var(--amber); color: var(--amber); background: rgba(245,158,11,0.08); }}
.chip {{ display: inline-block; padding: 0.1rem 0.35rem; margin: 0.1rem; background: rgba(15,23,42,0.5); border: 1px solid var(--border); border-radius: 4px; font-size: 0.72rem; color: var(--text-secondary); font-family: var(--font-mono); }}
.bar-container {{ background: rgba(15,23,42,0.5); border-radius: 4px; height: 8px; overflow: hidden; margin: 0.25rem 0; }}
.bar-fill {{ height: 100%; border-radius: 4px; background: linear-gradient(90deg, var(--amber), rgba(245,158,11,0.4)); transition: width 0.6s ease; }}
@media (max-width: 768px) {{ .tool-body {{ grid-template-columns: 1fr; }} }}
{extra_style}
</style>
</head>
<body>
<div id="cursor-glow"></div><div id="cursor-dot"></div>
{HEADER}
<main class="container tool-page">
  <div class="tool-page-header">
    <a href="../../" class="back-link"><span>&larr;</span> back to tools</a>
    <div class="tool-badge">{badge}</div>
    <h1>{h1_text}</h1>
    <p>{desc}</p>
  </div>
  <div class="tool-body">
    {body_html}
  </div>
</main>
{FOOTER}
<script>
{CURSOR_JS}
{extra_js}
</script>
</body>
</html>'''

# ======================== TOOL 6: NEVERREPEAT ========================
neverrepeat_js = '''
var feedbackStore = [];
function addFeedback() {
  var f = document.getElementById("nr-input").value.trim(); if (!f) return;
  var category = categorizeFeedback(f);
  feedbackStore.push({text: f, category: category});
  renderPrompts();
  document.getElementById("nr-input").value = "";
}
function categorizeFeedback(t) {
  var l = t.toLowerCase();
  if (l.match(/style|tone|voice|wording|copy|readab/)) return "writing style";
  if (l.match(/logic|reason|think|argu|fallac|assum/)) return "reasoning";
  if (l.match(/code|bug|error|function|api|syntax|performance/)) return "technical";
  if (l.match(/design|ui|layout|color|typography|spacing/)) return "design";
  if (l.match(/process|workflow|step|order|sequence/)) return "process";
  return "general";
}
function renderPrompts() {
  var cats = {};
  feedbackStore.forEach(function(f) {
    if (!cats[f.category]) cats[f.category] = {count: 0, examples: []};
    cats[f.category].count++;
    if (cats[f.category].examples.length < 2) cats[f.category].examples.push(f.text);
  });
  var h = '<div class="result-section"><h4>feedback library</h4>';
  if (feedbackStore.length === 0) {h += '<div class="tool-output-placeholder">No feedback recorded yet.</div>';}
  else {
    h += '<div class="metric-grid"><div class="metric-box"><strong>'+feedbackStore.length+'</strong><span>total items</span></div><div class="metric-box"><strong>'+Object.keys(cats).length+'</strong><span>categories</span></div><div class="metric-box"><strong>'+(feedbackStore.length>0?'active':'ready')+'</strong><span>status</span></div></div>';
    for (var c in cats) {
      h += '<div class="result-section"><h4>'+c+' ('+cats[c].count+' items)</h4>';
      h += '<div class="highlight-block">Prompt template: "When reviewing '+c+', check that... [based on '+cats[c].count+' past feedback items]"</div>';
      cats[c].examples.forEach(function(ex) {
        h += '<div style="font-size:0.75rem;color:var(--text-muted);padding:0.2rem 0;border-bottom:1px solid var(--border);font-family:var(--font-mono)">'+ex.substring(0,80)+(ex.length>80?'...':'')+'</div>';
      });
      h += '</div>';
    }
  }
  document.getElementById("nr-output").innerHTML = h;
}
function loadSampleFeedback() {
  document.getElementById("nr-input").value = "The tone is too casual for this audience. Use more formal language and avoid contractions.";
  document.getElementById("input-stats").textContent = "ready";
}
'''
neverrepeat_body = '''<div class="tool-input-panel">
      <h3>feedback text</h3>
      <textarea id="nr-input" placeholder="Paste a piece of feedback you gave someone.&#10;&#10;The tool categorizes it and adds to your reusable prompt library." rows="8"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="addFeedback()">add to library</button>
        <button class="sample-btn" onclick="loadSampleFeedback()">sample</button>
        <span id="input-stats" style="font-size:0.72rem;color:var(--text-muted);font-family:var(--font-mono)"></span>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>prompt library</h3>
      <div id="nr-output"><div class="tool-output-placeholder">Add feedback to build your reusable prompt library.</div></div>
    </div>'''

# ======================== TOOL 7: COPYSCOUT ========================
copyscout_js = '''
function runCopyScout() {
  var code = document.getElementById("cs-code").value, guide = document.getElementById("cs-guide").value;
  if (!code || !guide) { document.getElementById("cs-output").innerHTML = '<div class="tool-output-placeholder">Enter both code and style guide.</div>'; return; }
  var issues = [];
  var lc = code.toLowerCase(), lg = guide.toLowerCase();
  if (lg.match(/sentence case|capitali[sz]e|title case/) && lc.match(/[A-Z][a-z]+ [A-Z][a-z]+ [A-Z]/) && !lc.match(/^[A-Z][a-z]/m)) issues.push({severity:"medium",type:"capitalization",detail:"Mixed case detected. Style guide suggests consistent casing."});
  if (lg.match(/oxford comma|serial comma/) && lc.match(/, \w+ and/) && !lc.match(/, and/)) issues.push({severity:"low",type:"punctuation",detail:"Missing Oxford comma in list."});
  if (lg.match(/active voice/) && lc.match(/was \w+ed by|were \w+ed by|is \w+ed by/)) issues.push({severity:"high",type:"voice",detail:"Passive voice detected. Style guide prefers active voice."});
  if (lg.match(/contraction/) && !lg.match(/no contraction|avoid contraction/) && lc.match(/\b(don't|can't|won't|it's|they're|we're|i'm|isn't|aren't)\b/)) issues.push({severity:"low",type:"contractions",detail:"Contractions found. Verify style guide allows them."});
  if (lc.match(/\b(utilize|leverage|synergize|optimize|facilitate|implementation|utilization)\b/)) { var buzz = (lc.match(/\b(utilize|leverage|synergize|optimize|facilitate)\b/g)||[]).length; issues.push({severity:"medium",type:"jargon",detail:buzz+" instances of jargon/buzzwords ("+lc.match(/\b(utilize|leverage|synergize)\b/gi)+"). Style guides prefer plain language."});}
  if (lc.match(/\b(click here|read more|learn more|here's|check this out)\b/i)) issues.push({severity:"low",type:"link text",detail:"Generic link text detected. Use descriptive link text."});
  var wordCount = code.trim().split(/\\s+/).length;
  if (lg.match(/max.*\d{3}|limit.*\d{2,3}/) && wordCount > 100) issues.push({severity:"medium",type:"length",detail:"Content may exceed style guide length limits ("+wordCount+" words)."});
  var h = '<div class="result-section"><h4>scan results</h4><div class="metric-grid"><div class="metric-box"><strong>'+issues.length+'</strong><span>issues found</span></div><div class="metric-box"><strong>'+wordCount+'</strong><span>words scanned</span></div><div class="metric-box"><strong>'+(issues.filter(function(i){return i.severity==="high"}).length)+'</strong><span>high severity</span></div></div></div>';
  if (issues.length === 0) {h += '<div class="result-section"><div class="highlight-block" style="border-left-color:rgba(245,158,11,0.3)">No inconsistencies found. Copy appears aligned with the style guide.</div></div>';}
  else {
    issues.forEach(function(iss, idx) {
      var color = iss.severity === "high" ? "var(--amber)" : iss.severity === "medium" ? "var(--text-secondary)" : "var(--text-muted)";
      h += '<div class="result-section" style="animation-delay:'+(idx*0.05)+'s"><h4 style="color:'+color+'">'+iss.severity+' | '+iss.type+'</h4><div class="highlight-block">'+iss.detail+'</div></div>';
    });
  }
  document.getElementById("cs-output").innerHTML = h;
}
function loadCSSample() {
  document.getElementById("cs-code").value = "Welcome to our platform! We are excited to have you here. Click here to get started and learn more about what we can do. Our team utilizes cutting-edge technology to facilitate your success.";
  document.getElementById("cs-guide").value = "Style: sentence case, active voice, no jargon, descriptive links, Oxford comma.";
}
'''
copyscout_body = '''<div class="tool-input-panel">
      <h3>paste code + style guide</h3>
      <textarea id="cs-code" placeholder="Paste UI copy or code text to scan..." rows="6" style="min-height:120px"></textarea>
      <textarea id="cs-guide" placeholder="Paste style guide rules..." rows="4" style="min-height:80px;margin-top:0.5rem"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="runCopyScout()">scan copy</button>
        <button class="sample-btn" onclick="loadCSSample()">load sample</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>flagged issues</h3>
      <div id="cs-output"><div class="tool-output-placeholder">Paste code and style guide, then click "scan copy".</div></div>
    </div>'''

# ======================== TOOL 8: VIBECHECK ========================
vibecheck_js = '''
var models = ["Claude 4","GPT-5","Gemini 2","Llama 4","DeepSeek-V4"];
var dims = ["Quality","Speed","Cost","Creativity","Reliability"];
var ratings = {};
var selModel = "Claude 4";
function selectModel(m) { selModel = m; document.querySelectorAll(".model-btn").forEach(function(b){b.classList.remove("active")}); document.querySelectorAll(".model-btn").forEach(function(b){if(b.textContent===m)b.classList.add("active")}); renderVibe(); }
function setRating(d, v) { if (!ratings[selModel]) ratings[selModel] = {}; ratings[selModel][d] = v; renderVibe(); }
function renderVibe() {
  var r = ratings[selModel] || {};
  var h = '<div class="result-section"><h4>'+selModel+'</h4><div class="metric-grid"><div class="metric-box"><strong>'+(Object.keys(r).length>0?Object.values(r).reduce(function(a,b){return a+b},0)/5:0).toFixed(0)+'</strong><span>avg score</span></div><div class="metric-box"><strong>'+(Object.keys(r).length)+'</strong><span>dimensions rated</span></div><div class="metric-box"><strong>'+(Object.keys(r).length===5?"complete":"partial")+'</strong><span>status</span></div></div></div>';
  dims.forEach(function(d) {
    var v = r[d] || 0;
    h += '<div class="result-section"><h4>'+d+'</h4><div class="bar-container"><div class="bar-fill" style="width:'+(v*20)+'%"></div></div><div style="display:flex;justify-content:space-between;font-size:0.72rem;color:var(--text-muted);font-family:var(--font-mono)"><span>1</span><span>'+v+'/5</span><span>5</span></div></div>';
  });
  h += '<div class="result-section"><h4>rate '+selModel+'</h4><div style="display:flex;flex-wrap:wrap;gap:0.35rem">';
  dims.forEach(function(d) {
    h += '<div style="margin-bottom:0.35rem"><div style="font-size:0.65rem;color:var(--text-muted);margin-bottom:0.2rem">'+d+'</div>';
    for (var i=1;i<=5;i++) {
      var active = (ratings[selModel]||{})[d]===i;
      h += '<button class="choice-btn '+(active?'active':'')+'" style="padding:0.15rem 0.4rem;min-width:24px;font-size:0.7rem" onclick="setRating(\''+d+'\','+i+')">'+i+'</button> ';
    }
    h += '</div>';
  });
  h += '</div></div>';
  if (Object.keys(ratings).length > 1) {
    h += '<div class="result-section"><h4>comparison</h4><ul>';
    for (var m in ratings) { if (m !== selModel) {
      var scores = Object.values(ratings[m]); var avg = scores.length > 0 ? (scores.reduce(function(a,b){return a+b},0)/scores.length).toFixed(1) : "—";
      h += '<li><span>'+m+'</span><span>'+avg+' avg across '+scores.length+' dims</span></li>';
    }}
    h += '</ul></div>';
  }
  document.getElementById("vc-output").innerHTML = h;
}
function renderModelButtons() {
  var h = '';
  models.forEach(function(m){h += '<button class="choice-btn model-btn '+(m==="Claude 4"?"active":"")+'" onclick="selectModel(\''+m+'\')">'+m+'</button> ';});
  document.getElementById("vc-models").innerHTML = h;
}
renderModelButtons();
renderVibe();
'''
vibecheck_body = '''<div class="tool-input-panel">
      <h3>select model</h3>
      <div id="vc-models" style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:var(--space-md)"></div>
      <h3>rate dimensions</h3>
      <div id="vc-rating-area" style="font-size:0.8rem;color:var(--text-muted)">Select a model above, then rate it on each dimension below.</div>
    </div>
    <div class="tool-output-panel">
      <h3>vibe card</h3>
      <div id="vc-output"><div class="tool-output-placeholder">Select a model and rate its dimensions.</div></div>
    </div>'''

# ======================== TOOL 9: MEMORYMINE ========================
memorymine_js = '''
function mineMemory() {
  var txt = document.getElementById("mm-input").value.trim();
  if (!txt || txt.split(/\\s+/).length < 15) { document.getElementById("mm-output").innerHTML = '<div class="tool-output-placeholder">Need more journal content. Aim for 50+ words.</div>'; return; }
  var w = txt.match(/\\b\\w+\\b/g)||[], sents = txt.match(/[^.!?\\n]+[.!?]+/g)||[txt];
  var themes = [];
  var emotionWords = txt.match(/\\b(happy|sad|angry|frustrated|excited|anxious|tired|grateful|worried|hopeful|stressed|calm|proud|guilty|ashamed|lost|confident|inspired|burnout|overwhelm|joy|fear|love|hate|regret|relief|dread|hope|disappointed|content|restless|doubt|trust)\\b/gi)||[];
  var workWords = txt.match(/\\b(project|deadline|meeting|team|code|build|ship|launch|client|boss|colleague|promotion|review|feedback|goal|task|job|career)\\b/gi)||[];
  var peopleWords = txt.match(/\\b(friend|family|partner|spouse|child|parent|mom|dad|sister|brother|roommate|neighbor|community|relationship|date)\\b/gi)||[];
  var actionWords = txt.match(/\\b(started|finished|quit|began|stopped|changed|decided|committed|failed|succeeded|tried|learned|grew|shifted|moved|left|joined|created|built|wrote)\\b/gi)||[];
  var timeWords = txt.match(/\\b(today|yesterday|this week|this month|last year|next|soon|eventually|finally|never|always|sometimes|often|rarely|recently|lately)\\b/gi)||[];
  var negWords = txt.match(/\\b(not|never|none|nothing|no one|can't|couldn't|shouldn't|won't|didn't|doesn't|isn't|wasn't|haven't|hasn't|don't|without|lack|miss|lost|failed|bad|terrible|awful|difficult|hard|struggle)\\b/gi)||[];
  var posWords = txt.match(/\\b(great|amazing|wonderful|excellent|fantastic|good|better|best|happy|love|enjoy|grateful|thankful|proud|excited|hopeful|peaceful|calm|clear|success|progress|growth|improve)\\b/gi)||[];
  var wordsCount = w.length, sentsCount = sents.length;
  var avgSentLen = (wordsCount / Math.max(sentsCount,1)).toFixed(1);
  var tone = negWords.length > posWords.length * 1.5 ? "reflective / challenging" : posWords.length > negWords.length * 1.5 ? "positive / forward-looking" : "balanced / introspective";
  var repeatWords = {}; w.forEach(function(wd){var l=wd.toLowerCase();if(l.length>3){repeatWords[l]=(repeatWords[l]||0)+1}}); var topRepeats = Object.entries(repeatWords).sort(function(a,b){return b[1]-a[1]}).slice(0,8);
  var freqWords = topRepeats.filter(function(x){return x[1]>2}).map(function(x){return x[0]}).join(", ") || "none stand out";
  var h = '';
  h += '<div class="metric-grid"><div class="metric-box"><strong>'+wordsCount+'</strong><span>words</span></div><div class="metric-box"><strong>'+emotionWords.length+'</strong><span>emotion signals</span></div><div class="metric-box"><strong>'+tone+'</strong><span>tone</span></div></div>';
  h += '<div class="result-section"><h4>emotional landscape</h4><div class="highlight-block">'+(emotionWords.length>0?emotionWords.map(function(e){return '<span class="chip">'+e.toLowerCase()+'</span>'}).join(" "):'Minimal emotional vocabulary in this entry.')+'</div></div>';
  if (workWords.length > 2) {h += '<div class="result-section"><h4>work themes ('+workWords.length+' signals)</h4><div class="highlight-block">'+workWords.map(function(e){return '<span class="chip">'+e.toLowerCase()+'</span>'}).join(" ")+'</div></div>';}
  if (peopleWords.length > 1) {h += '<div class="result-section"><h4>people & relationships</h4><div class="highlight-block">'+peopleWords.map(function(e){return '<span class="chip">'+e.toLowerCase()+'</span>'}).join(" ")+'</div></div>';}
  if (actionWords.length > 2) {h += '<div class="result-section"><h4>action patterns</h4><div class="highlight-block">'+actionWords.map(function(e){return '<span class="chip">'+e.toLowerCase()+'</span>'}).join(" ")+'</div></div>';}
  h += '<div class="result-section"><h4>repeated vocabulary</h4><div style="font-size:0.75rem;color:var(--text-muted);font-family:var(--font-mono)">'+freqWords+'</div></div>';
  var insight = tone.includes("challenging") ? 'Tone suggests a difficult period. Consider what support you might need.' : tone.includes("positive") ? 'Forward-looking tone. Capture what\'s driving the momentum.' : 'Balanced entry. Look for what\'s absent — what topics did you avoid?';
  h += '<div class="result-section"><h4>one insight</h4><div class="highlight-block">'+insight+'</div></div>';
  document.getElementById("mm-output").innerHTML = h;
}
function loadMMSample() {
  document.getElementById("mm-input").value = "This week was tough. I had three project deadlines converge and I felt completely overwhelmed. The team meeting on Tuesday was good though — we finally aligned on the architecture direction. I'm frustrated that the database migration took longer than expected, but proud that we caught the edge cases before they hit production. I keep thinking about whether I should ask for a promotion. I've been leading this project for six months and the results speak for themselves. But I'm anxious about the conversation. What if they say no? What if I'm not ready? My partner says I'm ready. My friends say I'm ready. Why can't I believe it?";
}
'''
memorymine_body = '''<div class="tool-input-panel">
      <h3>journal entry</h3>
      <textarea id="mm-input" placeholder="Paste a journal entry, diary page, or personal reflection.&#10;&#10;The tool surfaces patterns, emotional arcs, and blind spots." rows="10"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="mineMemory()">mine patterns</button>
        <button class="sample-btn" onclick="loadMMSample()">sample entry</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>patterns and insights</h3>
      <div id="mm-output"><div class="tool-output-placeholder">Paste a journal entry and click "mine patterns".</div></div>
    </div>'''

# ======================== TOOL 10: SPIRAL LITE ========================
spiral_js = '''
function draftContent() {
  var topic = document.getElementById("sl-topic").value.trim(), brief = document.getElementById("sl-brief").value.trim();
  if (!topic) { document.getElementById("sl-output").innerHTML = '<div class="tool-output-placeholder">Enter a topic to draft content.</div>'; return; }
  var variants = generateVariants(topic, brief);
  var h = '<div class="result-section"><h4>3 drafts scored</h4>';
  variants.forEach(function(v, i) { var score = v.score, pct = score*20;
    h += '<div class="result-section" style="animation-delay:'+(i*0.1)+'s"><h4>variant '+(i+1)+'</h4><div class="highlight-block">'+v.text+'</div><div style="margin-top:0.25rem"><div class="bar-container"><div class="bar-fill" style="width:'+pct+'%"></div></div><div style="display:flex;justify-content:space-between;font-size:0.65rem;color:var(--text-muted)"><span>'+v.label+'</span><span>'+v.score.toFixed(1)+'/5</span></div></div></div>';
  });
  var best = variants.sort(function(a,b){return b.score-a.score})[0];
  h += '<div class="result-section"><h4>best variant (improved)</h4><div class="highlight-block" style="border-left-color:var(--amber)">'+best.text+'</div><div style="font-size:0.72rem;color:var(--text-muted);margin-top:0.25rem">Score: '+best.score.toFixed(1)+'/5 | Status: ready for review</div></div>';
  document.getElementById("sl-output").innerHTML = h;
}
function generateVariants(topic, brief) {
  var starts = ["Here's what nobody tells you about "+topic+".", "Three things I learned about "+topic+" this year.", "The real problem with "+topic+" isn't what you think.", "I spent months figuring out "+topic+". Here's the shortcut.", topic+": a practical guide for people who build things."];
  var mid = brief ? " "+brief.substring(0,80)+". " : " The key insight is that most approaches miss the fundamental pattern. ";
  var ends = [" This changes how you think about the whole thing.", " Try this approach and see what shifts.", " The results speak for themselves."];
  return [
    {text: starts[0]+mid+ends[0], score: 3.5, label: "hook-driven"},
    {text: starts[2]+mid+ends[1], score: 4.2, label: "contrarian"},
    {text: starts[1]+mid+ends[2], score: 3.8, label: "list-style"}
  ];
}
function loadSLSample() {
  document.getElementById("sl-topic").value = "AI-assisted code review";
  document.getElementById("sl-brief").value = "Focus on practical workflow improvements, not theory. Target: senior engineers skeptical of AI tools.";
}
'''
spiral_body = '''<div class="tool-input-panel">
      <h3>topic + brief</h3>
      <textarea id="sl-topic" placeholder="What do you want to write about?" rows="3" style="min-height:60px"></textarea>
      <textarea id="sl-brief" placeholder="Optional brief: target audience, angle, constraints..." rows="4" style="min-height:70px;margin-top:0.5rem"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="draftContent()">draft content</button>
        <button class="sample-btn" onclick="loadSLSample()">sample</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>drafts</h3>
      <div id="sl-output"><div class="tool-output-placeholder">Enter a topic and brief, then click "draft content".</div></div>
    </div>'''

# ======================== TOOL 11: AGENTROSTER ========================
agentroster_js = '''
var agents = ["Claude Code","GPT Engineer","Cursor","Devin","Copilot","Replit Agent"];
var agentsData = { "Claude Code": {taste:"thoughtful, precise, good at architecture",strength:"code architecture, refactoring, edge cases",weakness:"faster with context, slower cold start",bestFor:"complex refactors, system design"}, "GPT Engineer": {taste:"fast, pragmatic, good at scaffolding",strength:"rapid prototyping, boilerplate, full-stack",weakness:"can miss subtle bugs, less thorough",bestFor:"prototypes, MVPs, quick scripts"}, "Cursor": {taste:"interactive, good at context, agentic",strength:"large codebase work, multi-file edits",weakness:"can be overly aggressive with changes",bestFor:"feature implementation, bug fixes"}, "Devin": {taste:"autonomous, good at planning",strength:"end-to-end tasks, debugging, deployment",weakness:"slow, expensive, can go down rabbit holes",bestFor:"complex multi-step tasks"}, "Copilot": {taste:"conversational, inline suggestions",strength:"code completion, simple tasks, learning",weakness:"limited context, no planning",bestFor:"boilerplate, simple functions"}, "Replit Agent": {taste:"creative, good at full apps",strength:"app generation, deployment, iteration",weakness:"quality varies, limited customization",bestFor:"side projects, MVPs, prototypes"}
};
var selectedAgents = [];
function toggleAgent(a) {
  var idx = selectedAgents.indexOf(a); if (idx >= 0) {selectedAgents.splice(idx,1)} else if (selectedAgents.length < 3) {selectedAgents.push(a)} else return;
  document.querySelectorAll(".agent-btn").forEach(function(b){b.classList.remove("active")}); selectedAgents.forEach(function(s){document.querySelectorAll(".agent-btn").forEach(function(b){if(b.textContent===s)b.classList.add("active")})});
  renderRoster();
}
function renderRoster() {
  var h = '<div class="result-section"><h4>your roster</h4>';
  if (selectedAgents.length === 0) {h += '<div class="tool-output-placeholder">Select 1-3 agents to compare their taste profiles.</div>';}
  else { h += '<div class="metric-grid"><div class="metric-box"><strong>'+selectedAgents.length+'</strong><span>agents selected</span></div><div class="metric-box"><strong>plus 3 max</strong><span>selection limit</span></div></div>';
    selectedAgents.forEach(function(a, i) { var d = agentsData[a];
      h += '<div class="result-section" style="animation-delay:'+(i*0.1)+'s"><h4>'+a+'</h4><ul><li><span>taste</span><span style="font-size:0.7rem">'+d.taste+'</span></li><li><span>strength</span><span style="font-size:0.7rem">'+d.strength+'</span></li><li><span>weakness</span><span style="font-size:0.7rem">'+d.weakness+'</span></li><li><span>best for</span><span style="font-size:0.7rem">'+d.bestFor+'</span></li></ul></div>';
    });
    if (selectedAgents.length > 1) {
      h += '<div class="result-section"><h4>recommended task routing</h4><div class="highlight-block">';
      if (selectedAgents.includes("Claude Code")) h += 'Complex architecture work: Claude Code | ';
      if (selectedAgents.includes("GPT Engineer")) h += 'Rapid prototyping: GPT Engineer | ';
      if (selectedAgents.includes("Cursor")) h += 'Feature implementation: Cursor | ';
      if (selectedAgents.includes("Devin")) h += 'Autonomous multi-step tasks: Devin | ';
      h += '</div></div>';
    }
  }
  document.getElementById("ar-output").innerHTML = h;
}
(function() { var h=''; agents.forEach(function(a){h+='<button class="choice-btn agent-btn" onclick="toggleAgent(\''+a+'\')">'+a+'</button> '}); document.getElementById("ar-list").innerHTML = h; })();
'''
agentroster_body = '''<div class="tool-input-panel">
      <h3>select agents</h3>
      <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.5rem">Choose 1-3 agents to compare personality and taste profiles.</p>
      <div id="ar-list" style="display:flex;flex-wrap:wrap;gap:0.35rem"></div>
    </div>
    <div class="tool-output-panel">
      <h3>taste profile comparison</h3>
      <div id="ar-output"><div class="tool-output-placeholder">Select agents above to see their taste profiles.</div></div>
    </div>'''

# ======================== TOOL 12: ADOPTIONMAP ========================
adoptionmap_js = '''
function runAdoptionMap() {
  var answers = { q1: document.querySelector('input[name="adopt-q1"]:checked'), q2: document.querySelector('input[name="adopt-q2"]:checked'), q3: document.querySelector('input[name="adopt-q3"]:checked'), q4: document.querySelector('input[name="adopt-q4"]:checked') };
  if (!answers.q1 || !answers.q2 || !answers.q3 || !answers.q4) { document.getElementById("am-output").innerHTML = '<div class="tool-output-placeholder">Answer all 4 questions to see your readiness dashboard.</div>'; return; }
  var scores = { tooling: 0, culture: 0, skills: 0, leadership: 0 };
  scores.tooling = answers.q1.value === "yes" ? 80 : answers.q1.value === "partial" ? 40 : 10;
  scores.culture = answers.q2.value === "yes" ? 75 : answers.q2.value === "partial" ? 40 : 10;
  scores.skills = answers.q3.value === "yes" ? 70 : answers.q3.value === "partial" : 40;
  scores.leadership = answers.q4.value === "yes" ? 90 : answers.q4.value === "partial" ? 50 : 15;
  var total = Math.round((scores.tooling + scores.culture + scores.skills + scores.leadership) / 4);
  var label = total >= 70 ? "high readiness" : total >= 40 ? "developing" : "early stage";
  var h = '<div class="result-section"><h4>readiness score</h4><div class="metric-grid"><div class="metric-box"><strong>'+total+'%</strong><span>'+label+'</span></div></div></div>';
  var dims = [["tooling access", scores.tooling], ["culture & permission", scores.culture], ["skills & training", scores.skills], ["leadership buy-in", scores.leadership]];
  dims.forEach(function(d, i) {
    h += '<div class="result-section" style="animation-delay:'+(i*0.05)+'s"><h4>'+d[0]+'</h4><div class="bar-container"><div class="bar-fill" style="width:'+d[1]+'%"></div></div><div style="display:flex;justify-content:space-between;font-size:0.65rem;color:var(--text-muted)"><span>0</span><span>'+d[1]+'/100</span><span>100</span></div></div>';
  });
  if (total < 50) {h += '<div class="result-section"><h4>blockers identified</h4><div class="highlight-block">Low readiness score suggests structural blockers. Top leverage point: '+(scores.leadership < 50 ? 'leadership buy-in — without CEO adoption, team adoption stalls.' : 'skills and training — invest in hands-on workshops, not policy docs.')+'</div></div>';}
  else {h += '<div class="result-section"><h4>next step</h4><div class="highlight-block">Good foundation. Focus on '+(scores.skills < scores.tooling ? 'upskilling — tooling access exceeds team ability to use it.' : 'deepening — move from experimental to production-grade AI workflows.')+'</div></div>';}
  document.getElementById("am-output").innerHTML = h;
}
'''
adoptionmap_body = '''<div class="tool-input-panel">
      <h3>team readiness survey</h3>
      <div style="font-size:0.82rem;color:var(--text-secondary);display:flex;flex-direction:column;gap:0.75rem">
        <div><div style="margin-bottom:0.2rem;font-size:0.75rem;color:var(--text-muted)">Q1: Does your team have access to paid AI tools?</div>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q1" value="yes"> Yes</label>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q1" value="partial"> Partial</label>
          <label style="font-size:0.8rem"><input type="radio" name="adopt-q1" value="no"> No</label></div>
        <div><div style="margin-bottom:0.2rem;font-size:0.75rem;color:var(--text-muted)">Q2: Does your culture encourage AI experimentation?</div>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q2" value="yes"> Yes</label>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q2" value="partial"> Some teams</label>
          <label style="font-size:0.8rem"><input type="radio" name="adopt-q2" value="no"> No</label></div>
        <div><div style="margin-bottom:0.2rem;font-size:0.75rem;color:var(--text-muted)">Q3: Has your team received AI training?</div>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q3" value="yes"> Yes</label>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q3" value="partial"> Self-taught</label>
          <label style="font-size:0.8rem"><input type="radio" name="adopt-q3" value="no"> No</label></div>
        <div><div style="margin-bottom:0.2rem;font-size:0.75rem;color:var(--text-muted)">Q4: Does leadership actively use AI?</div>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q4" value="yes"> Yes</label>
          <label style="margin-right:0.5rem;font-size:0.8rem"><input type="radio" name="adopt-q4" value="partial"> Some execs</label>
          <label style="font-size:0.8rem"><input type="radio" name="adopt-q4" value="no"> No</label></div>
      </div>
      <div class="tool-actions"><button class="btn btn-primary" onclick="runAdoptionMap()" style="margin-top:0.5rem">calculate readiness</button></div>
    </div>
    <div class="tool-output-panel">
      <h3>readiness dashboard</h3>
      <div id="am-output"><div class="tool-output-placeholder">Answer the 4 questions and click "calculate readiness".</div></div>
    </div>'''

# ======================== TOOL 13: PROMPTLEAGUE ========================
promotleague_js = '''
var teamData = [];
function addTeamMember() {
  var name = document.getElementById("pl-name").value.trim(); if (!name) return;
  var usage = parseInt(document.getElementById("pl-usage").value) || 0;
  var prompts = parseInt(document.getElementById("pl-prompts").value) || 0;
  var quality = parseInt(document.getElementById("pl-quality").value) || 0;
  teamData.push({name: name, usage: usage, prompts: prompts, quality: quality, score: Math.round((usage*0.3 + prompts*0.4 + quality*0.3))});
  document.getElementById("pl-name").value = ""; document.getElementById("pl-usage").value = ""; document.getElementById("pl-prompts").value = ""; document.getElementById("pl-quality").value = "";
  renderLeaderboard();
}
function renderLeaderboard() {
  var sorted = teamData.sort(function(a,b){return b.score-a.score});
  var h = '<div class="result-section"><h4>leaderboard</h4><div class="metric-grid"><div class="metric-box"><strong>'+teamData.length+'</strong><span>team members</span></div><div class="metric-box"><strong>'+(teamData.length>0?sorted[0].score:0)+'</strong><span>top score</span></div><div class="metric-box"><strong>'+(teamData.length>0?sorted[0].name:'—')+'</strong><span>leader</span></div></div></div>';
  if (teamData.length===0) {h = '<div class="tool-output-placeholder">Add team members to see the leaderboard.</div>';}
  else { sorted.forEach(function(m, i) {
      var medal = i===0 ? "| gold" : i===1 ? "| silver" : i===2 ? "| bronze" : "";
      h += '<div class="result-section"><h4>#'+(i+1)+' '+m.name+' <span style="font-weight:400;color:var(--text-muted)">'+medal+'</span></h4><ul><li><span>weekly usage</span><span>'+m.usage+'</span></li><li><span>prompts contributed</span><span>'+m.prompts+'</span></li><li><span>quality score</span><span>'+m.quality+'/10</span></li><li><span>overall score</span><span>'+m.score+'</span></li></ul></div>';
    });
    h += '<div class="result-section"><h4>trending</h4><div class="highlight-block">Top contributor: '+sorted[0].name+' ('+sorted[0].prompts+' prompts shared). Encourage sharing patterns that work.</div></div>';
  }
  document.getElementById("pl-output").innerHTML = h;
}
function loadPLSample() {
  teamData = [{name:"Sarah",usage:45,prompts:12,quality:8,score:Math.round(45*0.3+12*0.4+8*0.3)},{name:"Marcus",usage:38,prompts:8,quality:9,score:Math.round(38*0.3+8*0.4+9*0.3)},{name:"Alex",usage:52,prompts:5,quality:6,score:Math.round(52*0.3+5*0.4+6*0.3)},{name:"Priya",usage:28,prompts:15,quality:9,score:Math.round(28*0.3+15*0.4+9*0.3)}];
  renderLeaderboard();
}
'''
promotleague_body = '''<div class="tool-input-panel">
      <h3>add team member</h3>
      <div style="display:flex;flex-direction:column;gap:0.5rem">
        <input type="text" id="pl-name" placeholder="Name" style="background:transparent;border:1px solid var(--border);padding:0.4rem 0.6rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.8rem">
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.5rem">
          <input type="number" id="pl-usage" placeholder="Usage count" style="background:transparent;border:1px solid var(--border);padding:0.4rem 0.6rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.75rem">
          <input type="number" id="pl-prompts" placeholder="Prompts shared" style="background:transparent;border:1px solid var(--border);padding:0.4rem 0.6rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.75rem">
          <input type="number" id="pl-quality" placeholder="Quality (1-10)" style="background:transparent;border:1px solid var(--border);padding:0.4rem 0.6rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.75rem">
        </div>
      </div>
      <div class="tool-actions" style="margin-top:0.5rem">
        <button class="btn btn-primary" onclick="addTeamMember()">add member</button>
        <button class="sample-btn" onclick="loadPLSample()">load sample data</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>leaderboard and stats</h3>
      <div id="pl-output"><div class="tool-output-placeholder">Add team members or load sample data.</div></div>
    </div>'''

# ======================== TOOL 14: JOBRESHORE ========================
jobreshore_js = '''
function simulateSupport() {
  var query = document.getElementById("jr-input").value.trim();
  if (!query) { document.getElementById("jr-output").innerHTML = '<div class="tool-output-placeholder">Enter a customer query.'; return; }
  var categories = ["billing", "technical", "account", "feature request", "complaint", "general"];
  var lq = query.toLowerCase();
  var cat = "general";
  if (lq.match(/bill|charge|price|pay|refund|invoice/)) cat = "billing";
  else if (lq.match(/error|bug|crash|not working|install|setup|login|password/)) cat = "technical";
  else if (lq.match(/account|profile|delete|close|upgrade|downgrade|subscription/)) cat = "account";
  else if (lq.match(/wish|would love|feature|suggest|request|add|missing/)) cat = "feature request";
  else if (lq.match(/terrible|bad|awful|worst|angry|furious|unacceptable|complaint/)) cat = "complaint";
  var confidence = cat === "billing" || cat === "technical" ? Math.round(70 + Math.random() * 20) : cat === "account" ? Math.round(60 + Math.random() * 25) : Math.round(40 + Math.random() * 30);
  var tier = confidence > 80 ? "tier 1 (auto-resolve)" : confidence > 60 ? "tier 1+ (AI + templates)" : "tier 2 (human needed)";
  var responses = { "billing": "Thanks for reaching out about billing. I can help with payment questions, invoices, and plan changes. Could you share your account email so I can look up the details?", "technical": "Thanks for reporting this issue. Let me gather some diagnostic info. Could you try clearing your cache and refreshing? If the issue persists, please share your browser version and OS.", "account": "I can help with account management. For security, please verify your email on file and I'll assist with any account changes you need.", "feature request": "Thanks for the suggestion! Our product team reviews all feature requests. I'll log this and you'll get notified if it moves forward.", "complaint": "I understand your frustration and I apologize for the experience. Let me escalate this to our team who can make things right. Could you share more details about what happened?", "general": "Thanks for your message. I'd be happy to help. Could you share a bit more context so I can point you to the right resources?" };
  var h = '<div class="result-section"><h4>query analysis</h4><ul><li><span>category</span><span>'+cat+'</span></li><li><span>AI confidence</span><span>'+confidence+'%</span></li><li><span>routing</span><span>'+tier+'</span></li></ul></div>';
  h += '<div class="result-section"><h4>AI response</h4><div class="highlight-block">'+responses[cat]+'</div></div>';
  h += '<div class="result-section"><h4>human review notes</h4><div class="highlight-block" style="border-left-color:var(--text-muted)">'+(confidence>80?'Response approved for auto-send. No human review needed.'+' Suggested follow-up: check billing system for recent activity.' : confidence>60?'Suggested response: use the AI draft with minor tone adjustments.'+' Flag for review: verify account details before sending.' : 'Escalate to senior support. This requires human judgment.')+'</div></div>';
  h += '<div class="result-section"><h4>cost calculation</h4><ul><li><span>AI handling cost</span><span>$0.05</span></li><li><span>human review cost</span><span>'+(confidence>80?'$0.00 (auto)':confidence>60?'$1.50 (light review)':'$5.00 (full review)')+'</span></li><li><span>vs traditional support</span><span>$8.50 saved</span></li></ul></div>';
  document.getElementById("jr-output").innerHTML = h;
}
function loadJRQuery() {
  document.getElementById("jr-input").value = "I was charged twice for my subscription this month. I need a refund for the duplicate charge.";
}
'''
jobreshore_body = '''<div class="tool-input-panel">
      <h3>customer query</h3>
      <textarea id="jr-input" placeholder="Paste a customer support query..." rows="6"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="simulateSupport()">simulate response</button>
        <button class="sample-btn" onclick="loadJRQuery()">sample query</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>AI response + human review</h3>
      <div id="jr-output"><div class="tool-output-placeholder">Enter a customer query and click "simulate response".</div></div>
    </div>'''

# ======================== TOOL 15: AGENTGARDENER ========================
agentgardener_js = '''
var agentsStatus = [
  {name:"Claudie",type:"Slack Agent",status:"healthy",uptime:"99.8%",tasks:142,errors:3,lastActive:"2 min ago",notes:"All clear"},
  {name:"Codex",type:"Code Agent",status:"healthy",uptime:"98.5%",tasks:89,errors:1,lastActive:"5 min ago",notes:"Handled PR review queue"},
  {name:"DataBot",type:"Data Agent",status:"degraded",uptime:"95.2%",tasks:56,errors:8,lastActive:"18 min ago",notes:"API rate limiting — review queue"},
  {name:"Writer",type:"Content Agent",status:"healthy",uptime:"99.1%",tasks:34,errors:0,lastActive:"1 hour ago",notes:"Idle"},
  {name:"Monitor",type:"Watchdog Agent",status:"error",uptime:"88.3%",tasks:12,errors:5,lastActive:"3 hours ago",notes:"Needs restart — memory leak detected"},
  {name:"DeployBot",type:"CI/CD Agent",status:"healthy",uptime:"99.9%",tasks:210,errors:0,lastActive:"30 sec ago",notes:"Active"}
];
function renderGardener() {
  var healthy = agentsStatus.filter(function(a){return a.status==="healthy"}).length;
  var degraded = agentsStatus.filter(function(a){return a.status==="degraded"}).length;
  var error = agentsStatus.filter(function(a){return a.status==="error"}).length;
  var h = '<div class="result-section"><h4>fleet overview</h4><div class="metric-grid"><div class="metric-box"><strong>'+agentsStatus.length+'</strong><span>total agents</span></div><div class="metric-box"><strong style="color:rgba(245,158,11,0.7)">'+healthy+'</strong><span>healthy</span></div><div class="metric-box"><strong style="color:var(--amber)">'+degraded+'</strong><span>degraded</span></div><div class="metric-box"><strong>'+error+'</strong><span>errors</span></div></div></div>';
  agentsStatus.forEach(function(a) {
    var color = a.status === "healthy" ? "rgba(245,158,11,0.6)" : a.status === "degraded" ? "var(--amber)" : "#ef4444";
    var barW = a.status === "healthy" ? 85 + Math.round(Math.random()*15) : a.status === "degraded" ? 50 + Math.round(Math.random()*25) : 25 + Math.round(Math.random()*20);
    h += '<div class="result-section" style="border:1px solid var(--border);padding:var(--space-sm);border-radius:var(--radius-sm)"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.25rem"><h4 style="margin:0;opacity:1">'+a.name+'</h4><span style="font-size:0.65rem;color:'+color+';font-family:var(--font-heading);text-transform:uppercase">'+a.status+'</span></div><div style="font-size:0.7rem;color:var(--text-muted);margin-bottom:0.35rem">'+a.type+' | uptime: '+a.uptime+' | tasks: '+a.tasks+' | errors: '+a.errors+'</div><div class="bar-container"><div class="bar-fill" style="width:'+barW+'%;background:linear-gradient(90deg,'+color+',rgba(245,158,11,0.3))"></div></div><div style="font-size:0.7rem;color:var(--text-muted);margin-top:0.2rem">'+a.notes+' | last active: '+a.lastActive+'</div></div>';
  });
  var totalIntervention = agentsStatus.filter(function(a){return a.status!=="healthy"}).length;
  h += '<div class="result-section"><h4>human intervention needed</h4><div class="highlight-block">'+totalIntervention+' agent'+(totalIntervention>1?'s':'')+' need attention. Priority: Monitor (memory leak) followed by DataBot (API rate limiting).</div></div>';
  document.getElementById("ag-output").innerHTML = h;
}
renderGardener();
'''
agentgardener_body = '''<div class="tool-input-panel">
      <h3>agent fleet</h3>
      <div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:0.5rem">Live status dashboard. No input needed — data is simulated for demonstration.</div>
      <div class="tool-actions"><button class="btn btn-primary" onclick="renderGardener()">refresh status</button></div>
    </div>
    <div class="tool-output-panel">
      <h3>agent status dashboard</h3>
      <div id="ag-output"><div class="tool-output-placeholder">Loading agent status...</div></div>
    </div>'''

# ======================== TOOL 16: CLAUDIECAST ========================
claudiecast_js = '''
function formatHandoff() {
  var txt = document.getElementById("cc-input").value.trim();
  if (!txt || txt.split("\\n").filter(function(l){return l.trim()}).length < 2) { document.getElementById("cc-output").innerHTML = '<div class="tool-output-placeholder">Enter an agent-to-agent conversation. Use labels like "Agent A:" and "Agent B:".'; return; }
  var lines = txt.split("\\n").filter(function(l){return l.trim()});
  var entries = []; var currentAgent = "", currentText = "";
  for (var i=0;i<lines.length;i++) {
    var m = lines[i].match(/^([A-Za-z][A-Za-z0-9\s]*?):\\s(.+)$/);
    if (m) { if (currentAgent) entries.push({agent: currentAgent, text: currentText.trim()}); currentAgent = m[1].trim(); currentText = m[2]; }
    else { currentText += " " + lines[i]; }
  }
  if (currentAgent) entries.push({agent: currentAgent, text: currentText.trim()});
  if (entries.length===0) {entries.push({agent:"Agent A",text:txt});}
  var agents = [...new Set(entries.map(function(e){return e.agent}))];
  var counts = {}; agents.forEach(function(a){counts[a]=entries.filter(function(e){return e.agent===a}).length});
  var topAgent = agents.sort(function(a,b){return counts[b]-counts[a]})[0];
  var h = '<div class="result-section"><h4>handoff log</h4><div class="metric-grid"><div class="metric-box"><strong>'+entries.length+'</strong><span>messages</span></div><div class="metric-box"><strong>'+agents.length+'</strong><span>agents</span></div><div class="metric-box"><strong>'+topAgent+'</strong><span>most active</span></div></div></div>';
  entries.forEach(function(e, i) {
    var agentColor = agents.indexOf(e.agent) % 2 === 0 ? "var(--amber)" : "var(--text-muted)";
    h += '<div class="result-section" style="animation-delay:'+(i*0.03)+'s;border-left:2px solid '+agentColor+';padding-left:var(--space-sm);margin-bottom:0.5rem"><h4 style="color:'+agentColor+';opacity:1">'+e.agent+'</h4><div style="font-size:0.8rem;color:var(--text-secondary);line-height:1.6">'+e.text+'</div><div style="font-size:0.6rem;color:var(--text-muted);margin-top:0.2rem;font-family:var(--font-mono)">turn '+(i+1)+'</div></div>';
  });
  h += '<div class="result-section"><h4>context passed</h4><div class="highlight-block">'+entries.length+' turns across '+agents.length+' agent'+(agents.length>1?'s':'')+'. Full context preserved for next agent handoff. Ready for downstream processing.</div></div>';
  document.getElementById("cc-output").innerHTML = h;
}
function loadCCSample() {
  document.getElementById("cc-input").value = "Codex: Found the bug in the payment processing module. The issue is a race condition in the retry logic.\nClaudie: Got it. What's the impact?\nCodex: About 0.3% of transactions fail silently. Users don't see an error, but the payment never completes.\nClaudie: That explains the support tickets about missing confirmations. Can you create a fix?\nCodex: Yes, adding a mutex to the retry handler. I'll have a PR in 30 minutes.\nClaudie: Perfect. I'll watch for the PR and queue it for Nitesh's review.";
}
'''
claudiecast_body = '''<div class="tool-input-panel">
      <h3>agent messages</h3>
      <textarea id="cc-input" placeholder="Paste agent-to-agent conversation with labels.&#10;&#10;Agent A: message text&#10;Agent B: response text" rows="10"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="formatHandoff()">format handoff</button>
        <button class="sample-btn" onclick="loadCCSample()">sample</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>handoff log</h3>
      <div id="cc-output"><div class="tool-output-placeholder">Enter conversation messages and click "format handoff".</div></div>
    </div>'''

# ======================== TOOL 17: SUPPORTLOOP ========================
supportloop_js = '''
function generateBugReport() {
  var desc = document.getElementById("sl2-desc").value.trim();
  if (!desc || desc.split(/\\s+/).length < 5) { document.getElementById("sl2-output").innerHTML = '<div class="tool-output-placeholder">Describe the issue in more detail (at least 5 words).</div>'; return; }
  var lc = desc.toLowerCase();
  var sections = ["Reproduction Steps", "Expected Behavior", "Actual Behavior", "Environment", "Impact Analysis", "Suggested Fix"];
  var cat = /error|crash|fail|broken|not working/.test(lc) ? "bug" : /slow|lag|delay|timeout|performance/.test(lc) ? "performance" : /ui|display|layout|alignment|styling|broken|missing/.test(lc) ? "ui" : "general";
  var sev = /crash|data loss|security|payment|billing|critical/.test(lc) ? "critical" : /broken|not working|wrong|incorrect/.test(lc) ? "high" : /slow|minor|cosmetic|typo|small/.test(lc) ? "low" : "medium";
  var steps = [];
  if (lc.match(/login|sign|auth|password/)) {steps.push("1. Navigate to login page");steps.push("2. Enter credentials");steps.push("3. Click submit");}
  else if (lc.match(/payment|checkout|cart|buy|purchase/)) {steps.push("1. Add item to cart");steps.push("2. Proceed to checkout");steps.push("3. Enter payment details");steps.push("4. Submit order");}
  else {steps.push("1. Navigate to the relevant page");steps.push("2. Perform the described action");steps.push("3. Observe the unexpected behavior");}
  var fixMatch = lc.match(/(?:fix|solution|should be|expected|need to) ([^.]+)/i);
  var fixSuggestion = fixMatch ? fixMatch[1].trim() : "Investigate the component and apply standard error handling.";
  var h = '<div class="result-section"><h4>bug report</h4><div class="metric-grid"><div class="metric-box"><strong>'+cat+'</strong><span>category</span></div><div class="metric-box"><strong style="color:'+(sev==="critical"?"#ef4444":"var(--amber)")+'">'+sev+'</strong><span>severity</span></div></div></div>';
  sections.forEach(function(s) {
    h += '<div class="result-section"><h4>'+s.replace(/([A-Z])/g," $1").trim()+'</h4><div class="highlight-block">';
    if (s === "Reproduction Steps") { steps.forEach(function(st){h+=st+"<br>"}); }
    else if (s === "Expected Behavior") { h += 'The system should '+(fixMatch?fixSuggestion:'function correctly without errors.')+' See: '+desc.substring(0,80)+'...'; }
    else if (s === "Actual Behavior") { h += desc.substring(0,200); }
    else if (s === "Environment") { h += 'Browser: Chrome 125 | OS: macOS 14.5 | App version: 2.4.1 (production)'; }
    else if (s === "Impact Analysis") { h += sev==="critical"?'Blocks core workflow for all users.' : sev==="high"?'Affects primary user flow.' : 'Minor impact, cosmetic or edge case.'; }
    else if (s === "Suggested Fix") { h += fixSuggestion; }
    h += '</div></div>';
  });
  h += '<div class="result-section"><h4>agent-ready summary</h4><div class="highlight-block" style="background:rgba(15,23,42,0.5)"><span style="font-family:var(--font-mono);font-size:0.78rem">BUG | '+sev+' | '+cat+' | '+desc.substring(0,60)+'... | Steps: '+(steps.length)+' | Suggested: '+fixSuggestion+'</span></div></div>';
  document.getElementById("sl2-output").innerHTML = h;
}
function loadSLBug() {
  document.getElementById("sl2-desc").value = "When I try to complete a payment, the page shows a loading spinner for 10+ seconds and then displays a generic error message. The payment doesn't go through but my card is still charged. This happens with multiple cards and browsers.";
}
'''
supportloop_body = '''<div class="tool-input-panel">
      <h3>issue description</h3>
      <textarea id="sl2-desc" placeholder="Describe the bug or issue you encountered.&#10;&#10;Include: what happened, what you expected, and any error messages." rows="8"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="generateBugReport()">generate report</button>
        <button class="sample-btn" onclick="loadSLBug()">sample bug</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>structured agent bug report</h3>
      <div id="sl2-output"><div class="tool-output-placeholder">Describe an issue and click "generate report".</div></div>
    </div>'''

# ======================== TOOL 18: NOTIONPLAN ========================
notionplan_js = '''
var planData = {};
function submitGoal() {
  var q1 = document.getElementById("np-q1").value.trim();
  var q2 = document.getElementById("np-q2").value.trim();
  var q3 = document.getElementById("np-q3").value.trim();
  var q4 = document.getElementById("np-q4").value.trim();
  if (!q1 || !q2 || !q3 || !q4) { document.getElementById("np-output").innerHTML = '<div class="tool-output-placeholder">Answer all 4 questions to generate your plan.</div>'; return; }
  planData = {goal: q1, blockers: q2, resources: q3, success: q4};
  var h = '<div class="result-section"><h4>quarterly plan</h4><div style="border:1px solid var(--border);border-radius:var(--radius-sm);padding:var(--space-sm);margin-bottom:var(--space-sm)">';
  h += '<div style="margin-bottom:0.75rem"><h4 style="opacity:1">primary goal</h4><div style="font-size:0.9rem;color:var(--text);font-family:var(--font-heading)">'+q1+'</div></div>';
  h += '<div style="margin-bottom:0.75rem"><h4 style="opacity:1">blockers + mitigations</h4><div style="font-size:0.82rem;color:var(--text-secondary)">'+q2+'</div></div>';
  h += '<div style="margin-bottom:0.75rem"><h4 style="opacity:1">resources required</h4><div style="font-size:0.82rem;color:var(--text-secondary)">'+q3+'</div></div>';
  h += '<div style="margin-bottom:0.75rem"><h4 style="opacity:1">success criteria</h4><div style="font-size:0.82rem;color:var(--text-secondary)">'+q4+'</div></div>';
  h += '</div>';
  h += '<div class="result-section"><h4>cross-reference check</h4><div class="highlight-block">Goal aligns with: company quarterly strategy | Potential conflict: resource allocation '+(q3.length>20?'may require cross-team coordination':'appears within team capacity')+' | Success metrics: '+(q4.length>15?'well-defined, measurable':'consider adding specific numeric targets')+'</div></div>';
  h += '<div class="result-section"><h4>action items</h4><ul><li><span>week 1-2</span><span>Validate assumptions, unblock resources</span></li><li><span>week 3-6</span><span>Execute core work, weekly check-ins</span></li><li><span>week 7-10</span><span>Mid-quarter review, adjust scope</span></li><li><span>week 11-12</span><span>Close out, document learnings</span></li></ul></div>';
  document.getElementById("np-output").innerHTML = h;
}
function loadNPSample() {
  document.getElementById("np-q1").value = "Ship the AI-assisted code review feature to all users by end of quarter";
  document.getElementById("np-q2").value = "Team capacity is tight — we have 3 other feature commitments. ML model accuracy needs 5% improvement before launch.";
  document.getElementById("np-q3").value = "1 additional ML engineer for 6 weeks, increased compute budget, 2 weeks of QA time";
  document.getElementById("np-q4").value = "Feature adopted by 30% of active users, review accuracy > 90%, less than 3 critical bugs reported in first month";
}
'''
notionplan_body = '''<div class="tool-input-panel">
      <h3>goal answers</h3>
      <div style="display:flex;flex-direction:column;gap:0.5rem">
        <div><div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.2rem">What is your primary goal this quarter?</div>
          <textarea id="np-q1" placeholder="Your primary goal..." rows="2" style="min-height:50px;width:100%;background:transparent;border:1px solid var(--border);padding:0.4rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.78rem"></textarea></div>
        <div><div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.2rem">What blockers do you anticipate?</div>
          <textarea id="np-q2" placeholder="Blockers and mitigations..." rows="2" style="min-height:50px;width:100%;background:transparent;border:1px solid var(--border);padding:0.4rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.78rem"></textarea></div>
        <div><div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.2rem">What resources do you need?</div>
          <textarea id="np-q3" placeholder="People, budget, tools..." rows="2" style="min-height:50px;width:100%;background:transparent;border:1px solid var(--border);padding:0.4rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.78rem"></textarea></div>
        <div><div style="font-size:0.72rem;color:var(--text-muted);margin-bottom:0.2rem">How will you measure success?</div>
          <textarea id="np-q4" placeholder="Success criteria..." rows="2" style="min-height:50px;width:100%;background:transparent;border:1px solid var(--border);padding:0.4rem;border-radius:var(--radius-sm);color:var(--text);font-family:var(--font-mono);font-size:0.78rem"></textarea></div>
      </div>
      <div class="tool-actions" style="margin-top:0.5rem">
        <button class="btn btn-primary" onclick="submitGoal()">generate plan</button>
        <button class="sample-btn" onclick="loadNPSample()">sample goal</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>structured plan document</h3>
      <div id="np-output"><div class="tool-output-placeholder">Answer all 4 questions and click "generate plan".</div></div>
    </div>'''

# ======================== TOOL 19: BENCHTUNNEL ========================
benchtunnel_js = '''
var models = ["GPT-5.5","Claude 4","Gemini 2.5","Llama 4","DeepSeek-V4"];
var challenges = ["React component refactor", "SQL query optimization", "API design", "Bug diagnosis", "Code review"];
var results = {};
function runBenchmark() {
  var model = document.querySelector(".model-bt-btn.active");
  var challenge = document.querySelector(".chal-btn.active");
  if (!model || !challenge) { document.getElementById("bt-output").innerHTML = '<div class="tool-output-placeholder">Select a model and challenge.</div>'; return; }
  var m = model.textContent, c = challenge.textContent;
  var score = Math.round(40 + Math.random() * 55);
  var speed = Math.round(30 + Math.random() * 65);
  var quality = Math.round(Math.random() * 10);
  var humanBaseline = 82;
  var prevScore = results[m] ? results[m].score : null;
  if (!results[m]) results[m] = {}; results[m] = {score: score, speed: speed, quality: quality, challenge: c};
  var h = '<div class="result-section"><h4>'+m+' | '+c+'</h4><div class="metric-grid"><div class="metric-box"><strong>'+score+'/100</strong><span>overall score</span></div><div class="metric-box"><strong>'+speed+'/100</strong><span>execution speed</span></div><div class="metric-box"><strong>'+(humanBaseline)+'/100</strong><span>human baseline</span></div></div></div>';
  h += '<div class="result-section"><h4>score breakdown</h4><ul><li><span>correctness</span><span>'+(quality>6?'pass':'needs work')+'</span></li><li><span>code quality</span><span>'+quality+'/10</span></li><li><span>edge case handling</span><span>'+(score>60?'good':'limited')+'</span></li><li><span>vs human baseline</span><span>'+Math.abs(score - humanBaseline)+' pts '+(score>humanBaseline?'above':'below')+'</span></li></ul></div>';
  if (prevScore) h += '<div class="result-section"><h4>improvement</h4><div class="highlight-block">Previous score: '+prevScore+' | Current: '+score+' | '+(score>prevScore?'+':'-')+Math.abs(score-prevScore)+' pts change</div></div>';
  var gpt55 = results["GPT-5.5"]; var claude4 = results["Claude 4"];
  if (gpt55 && claude4) {
    h += '<div class="result-section"><h4>head to head</h4><div class="highlight-block">GPT-5.5: '+gpt55.score+' | Claude 4: '+claude4.score+' | Winner: '+(gpt55.score>claude4.score?'GPT-5.5':'Claude 4')+'</div></div>';
  }
  if (score < 60) h += '<div class="result-section"><h4>failure analysis</h4><div class="highlight-block">Score below threshold. Common failure modes: incomplete edge case coverage, suboptimal algorithm choice, missing error handling.</div></div>';
  else h += '<div class="result-section"><h4>verdict</h4><div class="highlight-block" style="border-left-color:rgba(245,158,11,0.4)">Score: '+score+'/100. '+(score>=70?'Production-ready with minor review.':'Needs senior engineer review before production use.')+'</div></div>';
  document.getElementById("bt-output").innerHTML = h;
}
(function(){var h="";models.forEach(function(m){h+='<button class="choice-btn model-bt-btn" onclick="document.querySelectorAll(\\'".model-bt-btn\\").forEach(function(b){b.classList.remove(\\"active\\")});this.classList.add(\\"active\\")">'+m+'</button> '});document.getElementById("bt-models").innerHTML=h;var h2="";challenges.forEach(function(c){h2+='<button class="choice-btn chal-btn" onclick="document.querySelectorAll(\\'".chal-btn\\").forEach(function(b){b.classList.remove(\\"active\\")});this.classList.add(\\"active\\")">'+c+'</button> '});document.getElementById("bt-challenges").innerHTML=h2;document.querySelector(".model-bt-btn").classList.add("active");document.querySelector(".chal-btn").classList.add("active")})();
'''
benchtunnel_body = '''<div class="tool-input-panel">
      <h3>select model + challenge</h3>
      <div style="margin-bottom:0.5rem;font-size:0.72rem;color:var(--text-muted)">Model</div>
      <div id="bt-models" style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:var(--space-sm)"></div>
      <div style="margin-bottom:0.5rem;font-size:0.72rem;color:var(--text-muted)">Challenge</div>
      <div id="bt-challenges" style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:var(--space-sm)"></div>
      <div class="tool-actions"><button class="btn btn-primary" onclick="runBenchmark()">run benchmark</button></div>
    </div>
    <div class="tool-output-panel">
      <h3>score breakdown</h3>
      <div id="bt-output"><div class="tool-output-placeholder">Select a model and challenge, then click "run benchmark".</div></div>
    </div>'''

# ======================== TOOL 20: RIDETHEMODEL ========================
ridethemodel_js = '''
var taskStore = [];
function addTask() {
  var t = document.getElementById("rtm-input").value.trim(); if (!t) return;
  taskStore.push({task: t, scores: {}});
  document.getElementById("rtm-input").value = ""; renderScorecard();
}
function scoreTask(idx, model, score) {
  taskStore[idx].scores[model] = parseInt(score);
  renderScorecard();
}
function renderScorecard() {
  var models = ["GPT-5","Claude 4","Gemini 2","DeepSeek-V4"];
  if (taskStore.length === 0) { document.getElementById("rtm-output").innerHTML = '<div class="tool-output-placeholder">Add tasks and score each model to build your scorecard.</div>'; return; }
  var h = '<div class="result-section"><h4>personal model scorecard</h4><div class="metric-grid"><div class="metric-box"><strong>'+taskStore.length+'</strong><span>tasks</span></div><div class="metric-box"><strong>'+models.length+'</strong><span>models tracked</span></div></div></div>';
  taskStore.forEach(function(tsk, i) {
    h += '<div class="result-section"><h4>task '+(i+1)+': '+tsk.task.substring(0,50)+'</h4><div style="display:flex;flex-wrap:wrap;gap:0.5rem">';
    models.forEach(function(m) {
      var val = tsk.scores[m] || 0;
      h += '<div style="min-width:100px"><div style="font-size:0.65rem;color:var(--text-muted);margin-bottom:0.2rem">'+m+'</div><select class="choice-btn" style="padding:0.15rem 0.3rem;font-size:0.7rem;font-family:var(--font-mono);cursor:pointer" onchange="scoreTask('+i+',\''+m+'\',this.value)"><option value="0" '+(val===0?'selected':'')+'>—</option><option value="1" '+(val===1?'selected':'')+'>1</option><option value="2" '+(val===2?'selected':'')+'>2</option><option value="3" '+(val===3?'selected':'')+'>3</option><option value="4" '+(val===4?'selected':'')+'>4</option><option value="5" '+(val===5?'selected':'')+'>5</option></select></div>';
    });
    h += '</div></div>';
  });
  var totals = {}; var counts = {};
  models.forEach(function(m){totals[m]=0;counts[m]=0});
  taskStore.forEach(function(tsk){models.forEach(function(m){if(tsk.scores[m]){totals[m]+=tsk.scores[m];counts[m]++}})});
  h += '<div class="result-section"><h4>model averages</h4><ul>';
  var sorted = models.sort(function(a,b){var av=a,avb=b;return (totals[b]/Math.max(counts[b],1))-(totals[a]/Math.max(counts[a],1))});
  sorted.forEach(function(m){var avg = counts[m]>0 ? (totals[m]/counts[m]).toFixed(1) : "—"; h += '<li><span>'+m+'</span><span>'+avg+'/5 across '+(counts[m])+' tasks</span></li>';});
  h += '</ul></div>';
  var best = sorted[0]; var bestAvg = counts[best]>0 ? (totals[best]/counts[best]).toFixed(1) : 0;
  h += '<div class="result-section"><h4>one takeaway</h4><div class="highlight-block">Best performer: '+best+' ('+bestAvg+'/5). Keep running your personal benchmark every model release.</div></div>';
  document.getElementById("rtm-output").innerHTML = h;
}
function loadRTMSample() {
  taskStore = [{task:"Generate a REST API from a natural language description",scores:{}},{task:"Refactor a React component to reduce re-renders",scores:{}},{task:"Write a complex SQL query with window functions",scores:{}}];
  renderScorecard();
}
'''
ridethemodel_body = '''<div class="tool-input-panel">
      <h3>your tasks</h3>
      <textarea id="rtm-input" placeholder="Enter a task you care about..." rows="2" style="min-height:50px"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="addTask()">add task</button>
        <button class="sample-btn" onclick="loadRTMSample()">sample tasks</button>
      </div>
      <div style="font-size:0.72rem;color:var(--text-muted);margin-top:0.5rem">Add 3-5 tasks and score each model on a 1-5 scale.</div>
    </div>
    <div class="tool-output-panel">
      <h3>model scorecard</h3>
      <div id="rtm-output"><div class="tool-output-placeholder">Add tasks and score each model.</div></div>
    </div>'''

# ======================== TOOL 21: SLOPFILTER ========================
slopfilter_js = '''
function analyzeSlop() {
  var txt = document.getElementById("sf-input").value.trim();
  if (!txt || txt.split(/\\s+/).length < 10) { document.getElementById("sf-output").innerHTML = '<div class="tool-output-placeholder">Paste AI-generated work for review (at least 10 words).</div>'; return; }
  var w = txt.match(/\\b\\w+\\b/g)||[], sents = txt.match(/[^.!?\\n]+[.!?]+/g)||[txt];
  var signals = [];
  var reps = 0; var seen={}; w.forEach(function(wd){var l=wd.toLowerCase();if(l.length>3){if(seen[l])reps++;seen[l]=true}});
  var repRate = reps / Math.max(w.length,1);
  if (repRate > 0.15) signals.push({type:"repetitive vocabulary", severity:"medium", detail:"High word repetition suggests AI generation ("+(repRate*100).toFixed(0)+"% repeated words)."});
  var avgSentLen = w.length / Math.max(sents.length,1);
  if (avgSentLen < 8) signals.push({type:"short, choppy sentences", severity:"low", detail:"Average sentence length under 8 words — possible AI simplification."});
  if (avgSentLen > 28) signals.push({type:"unusually long sentences", severity:"low", detail:"Average sentence length over 28 words — check for AI verbosity."});
  var buzz = (txt.match(/\\b(delve|leverage|utilize|cutting-edge|synergy|revolutionary|game-changing|transformative|groundbreaking|paradigm|robust|seamless|intuitive|ecosystem|holistic|actionable|best-in-class)\\b/gi)||[]).length;
  if (buzz > 2) signals.push({type:"buzzword density", severity:"high", detail:buzz+" buzzwords detected. AI-generated content often leans on corporate jargon."});
  var quals = (txt.match(/\\b(significantly|notably|importantly|essentially|basically|virtually|practically|arguably|undoubtedly|certainly)\\b/gi)||[]).length;
  if (quals > 3) signals.push({type:"hedging qualifiers", severity:"medium", detail:quals+" qualifiers found — AI hedging language that lacks specific evidence."});
  var lists = txt.match(/\\d+\\.\\s/g)||[];
  if (lists.length > 3) signals.push({type:"list-heavy structure", severity:"low", detail:lists.length+" numbered items. AI often overuses lists."});
  var confidentWords = (txt.match(/\\b(always|never|everyone|nobody|everything|nothing|all|none)\\b/gi)||[]).length;
  if (confidentWords > 3) signals.push({type:"over-generalization", severity:"medium", detail:"Absolute language ("+confidentWords+" instances) suggests AI overconfidence."});
  var confidence = Math.max(10, Math.min(95, 100 - (signals.length * 12 + buzz * 5 + reps * 2)));
  var routing = confidence >= 80 ? "auto-approve" : confidence >= 50 ? "flag for review" : "reject / rewrite";
  var color = confidence >= 80 ? "rgba(245,158,11,0.5)" : confidence >= 50 ? "var(--amber)" : "#ef4444";
  var h = '<div class="result-section"><h4>confidence score</h4><div style="text-align:center;padding:var(--space-md)"><div style="font-size:3rem;font-weight:700;font-family:var(--font-heading);color:'+color+'">'+confidence+'%</div><div style="font-size:0.72rem;color:var(--text-muted);margin-top:0.25rem;text-transform:uppercase;letter-spacing:0.1em">'+routing+'</div></div></div>';
  h += '<div class="result-section"><h4>signals detected</h4><div class="metric-grid"><div class="metric-box"><strong>'+signals.length+'</strong><span>signals</span></div><div class="metric-box"><strong>'+w.length+'</strong><span>words analyzed</span></div></div></div>';
  if (signals.length === 0) {h += '<div class="result-section"><div class="highlight-block" style="border-left-color:rgba(245,158,11,0.3)">No AI-generation signals detected. Content appears human-written.</div></div>';}
  else { signals.forEach(function(s, i) {
      h += '<div class="result-section" style="animation-delay:'+(i*0.05)+'s"><h4 style="color:'+(s.severity==="high"?"var(--amber)":"var(--text-muted)")+'">'+s.severity+' | '+s.type+'</h4><div class="highlight-block">'+s.detail+'</div></div>';
    });
  }
  h += '<div class="result-section"><h4>routing recommendation</h4><div class="highlight-block" style="border-left-color:'+color+'">Confidence: '+confidence+'% | Routing: '+routing+' | '+(confidence>=80?'AI work approved for direct use.':'Send to senior reviewer before publishing.')+'</div></div>';
  document.getElementById("sf-output").innerHTML = h;
}
function loadSFSample() {
  document.getElementById("sf-input").value = "In today's rapidly evolving digital landscape, it is essential to leverage cutting-edge solutions that drive transformative outcomes. By utilizing our revolutionary platform, organizations can significantly enhance operational efficiency and achieve unprecedented levels of success. Our holistic ecosystem seamlessly integrates best-in-class features that empower teams to collaborate effectively and deliver actionable insights. Importantly, we believe that our game-changing approach fundamentally transforms the way businesses operate in this paradigm shift towards digital transformation. The robust architecture ensures that virtually every stakeholder can benefit from our intuitive interface, which is designed to facilitate seamless workflows and optimize productivity across the entire organization.";
}
'''
slopfilter_body = '''<div class="tool-input-panel">
      <h3>AI-generated work</h3>
      <textarea id="sf-input" placeholder="Paste AI-generated text for quality analysis..." rows="8"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="analyzeSlop()">analyze</button>
        <button class="sample-btn" onclick="loadSFSample()">sample AI text</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>confidence score + routing</h3>
      <div id="sf-output"><div class="tool-output-placeholder">Paste AI-generated work and click "analyze".</div></div>
    </div>'''

# ======================== TOOL 22: CLAUDIEPAIR ========================
claudiepair_js = '''
var editHistory = [];
function suggestEdits() {
  var txt = document.getElementById("cp-input").value;
  if (!txt || txt.trim().split(/\\s+/).length < 5) { document.getElementById("cp-output").innerHTML = '<div class="tool-output-placeholder">Enter at least 5 words for the agent to review.</div>'; return; }
  var sents = txt.match(/[^.!?\\n]+[.!?]+/g)||[txt];
  var edits = [];
  var wc = txt.trim().split(/\\s+/).length;
  if (wc > 100) edits.push({type:"length", detail:"Document exceeds 100 words. Consider breaking into sections."});
  var longSent = sents.filter(function(s){return s.split(/\\s+/).length > 35});
  longSent.forEach(function(s){edits.push({type:"sentence length", detail:'Sentence too long ('+s.split(/\\s+/).length+' words). Consider splitting for readability.', original: s.trim().substring(0,60)+'...'});});
  var passive = txt.match(/\\b(is|are|was|were|been|being) \\w+ed\\b/gi)||[];
  if (passive.length > 2) edits.push({type:"passive voice", detail:passive.length+' instances of passive voice. Try active voice for stronger impact.', original: passive.slice(0,2).join(", ")});
  var adverbs = txt.match(/\\b(very|really|quite|extremely|highly|absolutely|totally|completely|literally|just)\\b/gi)||[];
  if (adverbs.length > 2) edits.push({type:"adverb overuse", detail:adverbs.length+' weak adverbs. Consider stronger verbs instead.', original: adverbs.slice(0,3).join(", ")});
  var problems = txt.match(/\\b(issue|problem|challenge|difficult|hard)\\b/gi)||[];
  if (problems.length > 3) edits.push({type:"negative framing", detail:problems.length+' problem-focused words. Try reframing as opportunities.', original: 'e.g., "'+problems.slice(0,2).join(", ")+'"'});
  if (edits.length === 0) edits.push({type:"style check", detail:"No significant issues found. Clean writing with good readability."});
  var h = '<div class="result-section"><h4>agent review</h4><div class="metric-grid"><div class="metric-box"><strong>'+wc+'</strong><span>words</span></div><div class="metric-box"><strong>'+edits.length+'</strong><span>suggestions</span></div><div class="metric-box"><strong>'+(edits.filter(function(e){return e.type!=="style check"}).length===0?'clean':'needs polish')+'</strong><span>status</span></div></div></div>';
  edits.forEach(function(e, i) {
    h += '<div class="result-section" style="animation-delay:'+(i*0.05)+'s"><h4>'+(e.original?'suggestion | '+e.type:e.type)+'</h4><div class="highlight-block">'+e.detail+(e.original?'<br><span style="font-size:0.7rem;color:var(--text-muted);font-family:var(--font-mono)">Context: '+e.original+'</span>':'')+'</div></div>';
  });
  editHistory.push({text: txt, edits: edits.length, time: new Date().toLocaleTimeString()});
  h += '<div class="result-section"><h4>research note</h4><div class="highlight-block">Agent checked: style guides, common readability patterns, and word frequency analysis. '+(editHistory.length)+' revision'+(editHistory.length>1?'s':'')+' tracked this session.</div></div>';
  document.getElementById("cp-output").innerHTML = h;
}
function loadCPSample() {
  document.getElementById("cp-input").value = "The main issue with our current approach is that the implementation of the new feature is extremely difficult and faces a lot of challenges. The problem is that we have to completely rethink the architecture which is very complex and really hard to do in the current timeline that we have. There are quite a few things that need to be addressed before we can move forward with the project.";
}
'''
claudiepair_body = '''<div class="tool-input-panel">
      <h3>write text</h3>
      <textarea id="cp-input" placeholder="Start writing. The agent watches and suggests edits as you work." rows="10"></textarea>
      <div class="tool-actions">
        <button class="btn btn-primary" onclick="suggestEdits()">get agent edits</button>
        <button class="sample-btn" onclick="loadCPSample()">sample text</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>agent-suggested edits</h3>
      <div id="cp-output"><div class="tool-output-placeholder">Write text and click "get agent edits" for suggestions.</div></div>
    </div>'''

# ======================== TOOL 23: SUPERAGENT SETUP ========================
superagent_js = '''
var config = { integrations: [], tools: [], permissions: "" };
function toggleIntegration(i) { var idx = config.integrations.indexOf(i); idx >= 0 ? config.integrations.splice(idx,1) : config.integrations.push(i); updateSetup(); }
function toggleTool(t) { var idx = config.tools.indexOf(t); idx >= 0 ? config.tools.splice(idx,1) : config.tools.push(t); updateSetup(); }
function setPerm(p) { config.permissions = p; updateSetup(); }
function updateSetup() {
  var h = '<div class="result-section"><h4>setup configuration</h4><div class="metric-grid"><div class="metric-box"><strong>'+config.integrations.length+'</strong><span>integrations</span></div><div class="metric-box"><strong>'+config.tools.length+'</strong><span>tools enabled</span></div><div class="metric-box"><strong>'+config.permissions||'not set'+'</strong><span>access level</span></div></div></div>';
  h += '<div class="result-section"><h4>setup guide</h4><div class="highlight-block">1. Create a Slack app with bot token<br>2. Add scopes: '+(config.integrations.includes("slack")?'channels:history, chat:write':' (select integrations first)')+'<br>3. Deploy agent service (Node.js or Python)<br>4. Connect data sources: '+(config.integrations.join(", ")||"none selected")+'<br>5. Configure permission: '+config.permissions||"select below" + '<br>6. Set up feedback loop (Slack channel for human review)<br>7. Test with a low-risk task first</div></div>';
  h += '<div class="result-section"><h4>dashboard preview</h4><div style="border:1px solid var(--border);border-radius:var(--radius-sm);padding:var(--space-sm);font-size:0.78rem;color:var(--text-secondary)"><div>Status: setup pending</div><div>Integrations: '+(config.integrations.length>0?config.integrations.join(", "):'none')+'</div><div>Agent name: super-agent (editable)</div><div>Team access: '+(config.permissions||"not configured")+'</div></div></div>';
  h += '<div class="result-section"><h4>estimated deployment</h4><ul><li><span>setup time</span><span>'+(config.integrations.length*15+30)+' minutes</span></li><li><span>maintenance</span><span>'+(config.tools.includes("monitoring")?'automated monitoring configured':'set up monitoring')+'</span></li><li><span>next step</span><span>connect to data warehouse</span></li></ul></div>';
  document.getElementById("sa-output").innerHTML = h;
}
'''
superagent_body = '''<div class="tool-input-panel">
      <h3>configure your agent</h3>
      <div style="margin-bottom:0.5rem;font-size:0.72rem;color:var(--text-muted)">Integrations (click to toggle)</div>
      <div style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:var(--space-sm)">
        <button class="choice-btn" onclick="toggleIntegration('slack')">Slack</button>
        <button class="choice-btn" onclick="toggleIntegration('github')">GitHub</button>
        <button class="choice-btn" onclick="toggleIntegration('notion')">Notion</button>
        <button class="choice-btn" onclick="toggleIntegration('linear')">Linear</button>
        <button class="choice-btn" onclick="toggleIntegration('docs')">Google Docs</button>
      </div>
      <div style="margin-bottom:0.5rem;font-size:0.72rem;color:var(--text-muted)">Tools</div>
      <div style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-bottom:var(--space-sm)">
        <button class="choice-btn" onclick="toggleTool('code-review')">Code Review</button>
        <button class="choice-btn" onclick="toggleTool('data-query')">Data Queries</button>
        <button class="choice-btn" onclick="toggleTool('monitoring')">Monitoring</button>
        <button class="choice-btn" onclick="toggleTool('content')">Content</button>
      </div>
      <div style="margin-bottom:0.5rem;font-size:0.72rem;color:var(--text-muted)">Permission level</div>
      <div style="display:flex;flex-wrap:wrap;gap:0.35rem">
        <button class="choice-btn" onclick="setPerm('read-only')">read-only</button>
        <button class="choice-btn" onclick="setPerm('read-write')">read-write</button>
        <button class="choice-btn" onclick="setPerm('admin')">admin</button>
      </div>
    </div>
    <div class="tool-output-panel">
      <h3>setup guide + dashboard</h3>
      <div id="sa-output"><div class="tool-output-placeholder">Toggle config options to build your setup guide.</div></div>
    </div>'''


# ======================== WRITE ALL FILES ========================
tools = [
    ("neverrepeat", "NeverRepeat | manager feedback coder", "Manager feedback coder. Every piece of feedback becomes a reusable prompt.", "tool 06 | interactive", "NeverRepeat", neverrepeat_body, neverrepeat_js),
    ("copyscout", "CopyScout | codebase copy enforcer", "Paste code plus style guide. Flags UI copy inconsistencies.", "tool 07 | interactive", "CopyScout", copyscout_body, copyscout_js),
    ("vibecheck", "VibeCheck | model review framework", "Select a model, rate 5 dimensions. Get a comparison card.", "tool 08 | interactive", "VibeCheck", vibecheck_body, vibecheck_js),
    ("memorymine", "MemoryMine | personal reflection tool", "Paste journal entries. Surface patterns and insights.", "tool 09 | interactive", "MemoryMine", memorymine_body, memorymine_js),
    ("spiral-lite", "Spiral Lite | content automation", "Enter a topic and brief. Drafts, scores, and improves content.", "tool 10 | interactive", "Spiral Lite", spiral_body, spiral_js),
    ("agentroster", "AgentRoster | agent personality comparison", "Select agents. Compare taste profiles and strengths.", "tool 11 | interactive", "AgentRoster", agentroster_body, agentroster_js),
    ("adoptionmap", "AdoptionMap | team AI readiness", "Answer survey questions. Get a readiness dashboard.", "tool 12 | interactive", "AdoptionMap", adoptionmap_body, adoptionmap_js),
    ("promotleague", "PromptLeague | usage stats dashboard", "Enter team data. Get leaderboard and usage statistics.", "tool 13 | interactive", "PromptLeague", promotleague_body, promotleague_js),
    ("jobreshore", "JobReshore | AI support simulator", "Enter a customer query. Get AI response plus human review.", "tool 14 | interactive", "JobReshore", jobreshore_body, jobreshore_js),
    ("agentgardener", "AgentGardener | agent health dashboard", "Simulated agent status cards with health metrics.", "tool 15 | interactive", "AgentGardener", agentgardener_body, agentgardener_js),
    ("claudiecast", "ClaudieCast | agent conversation viewer", "Paste messages. Get formatted handoff log.", "tool 16 | interactive", "ClaudieCast", claudiecast_body, claudiecast_js),
    ("supportloop", "SupportLoop | bug report generator", "Describe an issue. Get structured agent bug report.", "tool 17 | interactive", "SupportLoop", supportloop_body, supportloop_js),
    ("notionplan", "NotionPlan | quarterly planning tool", "Answer goal questions. Get structured plan document.", "tool 18 | interactive", "NotionPlan", notionplan_body, notionplan_js),
    ("benchtunnel", "BenchTunnel | model benchmark", "Select model + challenge. Get score breakdown.", "tool 19 | interactive", "BenchTunnel", benchtunnel_body, benchtunnel_js),
    ("ridethemodel", "RideTheModel | model test suite", "Enter tasks. Get personal model scorecard.", "tool 20 | interactive", "RideTheModel", ridethemodel_body, ridethemodel_js),
    ("slopfilter", "SlopFilter | review triage for AI work", "Paste AI content. Get confidence score and routing.", "tool 21 | interactive", "SlopFilter", slopfilter_body, slopfilter_js),
    ("claudiepair", "ClaudiePair | collaborative document", "Write text. Get agent-suggested edits.", "tool 22 | interactive", "ClaudiePair", claudiepair_body, claudiepair_js),
    ("superagentsetup", "SuperAgent Setup | agent scaffold wizard", "Toggle config. Get setup guide and dashboard.", "tool 23 | interactive", "SuperAgent Setup", superagent_body, superagent_js),
]

for name, title, desc, badge, h1, body, js in tools:
    html = base_html(title, desc, badge, h1, body, extra_js=js)
    path = os.path.join(BASE, name, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {path} ({len(html)} bytes)")

print(f"\nDone! {len(tools)} tool pages generated.")
