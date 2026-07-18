"""
All lesson content lives here. To add a new lesson, add a dict to LESSONS
with at least: slug, title, topic, order.

A lesson is "playable" (has a working editor + challenge) once you fill in:
  story_html, starter_code, check_pattern, placeholder, xp

Until then it renders as a "coming soon" stub on the path, so you can plan
the whole curriculum before writing every lesson.
"""

LESSONS = [
    {
        "slug": "print-statements",
        "title": "Print Statements",
        "subtitle": "Your First Line of Code",
        "topic": "Basics",
        "order": 1,
        "xp": 50,
        "story_html": (
            "<p><code>print()</code> is how you make Python actually show something. "
            "Whatever you put between the quotes shows up on screen exactly as written "
            "— that's the whole lesson. This is the first thing every Python program "
            "learns to do.</p>"
            "<p>The quotes matter: <code>\"Hello, PYGO!\"</code> is text (Python calls it "
            "a <em>string</em>). Anything inside quotes prints exactly as-is, spelling "
            "and all.</p>"
        ),
        "challenge_html": (
            "Change the text between the quotes to anything you want, then hit Run. "
            "Just make it say something other than <strong>Hello, PYGO!</strong>"
        ),
        "starter_code": 'print("Hello, PYGO!")  # change the text between the quotes',
        "check_pattern": r"(.+)",
        "placeholder_value": "Hello, PYGO!",
        "success_message": "You just ran your first line of Python.",
    },
   {
        "slug": "variables",
        "title": "Variables",
        "subtitle": "The Labeled Box",
        "topic": "Basics",
        "order": 2,
        "xp": 50,
        "story_html": (
            "<p>A variable is a labeled box. You write a name, you put something "
            "inside, and you can grab it back later just by using that name.</p>"
            "<p><code>message = \"Welcome to PYGO!\"</code> creates a box called "
            "<strong>message</strong> holding that text. You just used "
            "<code>print()</code> on plain text — now try it on a variable instead. "
            "Same idea, Python just looks inside the box first.</p>"
        ),
        "challenge_html": (
            "Change <strong>\"Welcome to PYGO!\"</strong> to any other message, "
            "then hit Run. The output should show your new message, not the original one."
        ),
        "starter_code": 'message = "Welcome to PYGO!"\n\nprint(message)',
        "check_pattern": r"(.+)",
        "placeholder_value": "Welcome to PYGO!",
        "success_message": "You bound your first variable.",
    },
    {
        "slug": "f-strings",
        "title": "f-Strings",
        "subtitle": "Mixing Variables Into Text",
        "topic": "Basics",
        "order": 3,
        "xp": 50,
        "story_html": (
            "<p>Last lesson you printed a variable on its own. Sometimes you want to "
            "mix a variable <em>into</em> a sentence instead — that's what an "
            "f-string is for.</p>"
            "<p>Put an <code>f</code> right before the opening quote, then wrap any "
            "variable name in <code>{ }</code> inside the string. Python swaps in "
            "whatever that variable holds. <code>f\"Hi, {name}!\"</code> becomes "
            "<code>\"Hi, Ava!\"</code> if <code>name</code> is <code>\"Ava\"</code>.</p>"
        ),
        "challenge_html": (
            "Change <strong>\"Ava\"</strong> to your own name, then hit Run. "
            "Output should read <strong>Hi, &lt;your name&gt;!</strong>, not "
            "<strong>Hi, Ava!</strong>"
        ),
        "starter_code": 'name = "Ava"  # change me\n\nprint(f"Hi, {name}!")',
        "check_pattern": r"Hi,\s*(.+)!",
        "placeholder_value": "Ava",
        "success_message": "You mixed a variable right into a sentence.",
    },
    {
        "slug": "data-types",
        "title": "Data Types",
        "subtitle": "What's Inside the Box",
        "topic": "Basics",
        "order": 4,
        "xp": 50,
        "story_html": (
            "<p>Every box doesn't just hold a value — it holds a <strong>type</strong> of value. "
            "Text is a <code>str</code>. Whole numbers are an <code>int</code>. Numbers with a "
            "decimal point are a <code>float</code>. True/false is a <code>bool</code>.</p>"
            "<p>Python figures out the type automatically from what you put in the box, and the "
            "type decides what you're allowed to do with it. You can multiply two numbers. You "
            "can't multiply two sentences — that's a mismatch Python won't let you make by accident.</p>"
            "<p>Multiply an <code>int</code> by a <code>float</code> and Python upgrades the result "
            "to a <code>float</code> automatically, so the decimal never gets lost.</p>"
        ),
        "challenge_html": (
            "Change <strong>quantity</strong> and <strong>price_each</strong> to real numbers, "
            "then hit Run. Your output should read <strong>Total: $&lt;number&gt;</strong> with "
            "something other than the starting total."
        ),
        "starter_code": (
            "quantity = 1        # change me - how many items?\n"
            "price_each = 1.0    # change me - price of one item\n\n"
            "total = quantity * price_each\n"
            'print(f"Total: ${total}")'
        ),
        "check_pattern": r"Total:\s*\$(\d+(?:\.\d+)?)",
        "placeholder_value": "1.0",
        "success_message": "You worked out a real total using int and float together.",
    },
   {
        "slug": "strings",
        "title": "Strings",
        "subtitle": "Working with Text",
        "topic": "Basics",
        "order": 5,
        "xp": 50,
        "story_html": (
            "<p>Text lives in a box just like anything else — Python calls it a "
            "<code>str</code>, short for string. Anything inside quotes, single or double, "
            "is a string.</p>"
            "<p>You can glue two strings together with <code>+</code>. "
            "<code>\"PY\" + \" \" + \"GO\"</code> becomes <code>\"PY GO\"</code> — "
            "notice the <code>\" \"</code> in the middle, that's a space you have to add yourself, "
            "Python won't add it for you.</p>"
            "<p>Handy string tools worth knowing: <code>.upper()</code> and <code>.lower()</code> "
            "change case, <code>len(text)</code> tells you how many characters are in it.</p>"
        ),
        "challenge_html": (
            "Right now <strong>full_name</strong> is only holding <strong>first_name</strong>. "
            "Combine <strong>first_name</strong> and <strong>last_name</strong> with a space "
            "between them, then hit Run. Output should read <strong>Hello, PY GO!</strong>"
        ),
        "starter_code": (
            'first_name = "PY"\n'
            'last_name = "GO"\n\n'
            "full_name = first_name  # combine first_name and last_name here\n\n"
            'print(f"Hello, {full_name}!")'
        ),
        "check_pattern": r"Hello,\s*(.+?)!",
        "placeholder_value": "PY",
        "success_message": "You combined two strings into one.",
    },
{
        "slug": "numbers-math",
        "title": "Numbers & Math",
        "subtitle": "Doing the Arithmetic",
        "topic": "Basics",
        "order": 6,
        "xp": 50,
        "story_html": (
            "<p>Python does normal math with <code>+ - * /</code>, but it also has two "
            "operators most languages hide from you: <code>//</code> (floor division) gives "
            "you the whole-number result and throws away the remainder, and <code>%</code> "
            "(modulo) gives you <em>only</em> the remainder.</p>"
            "<p><code>125 // 60</code> is <code>2</code> — two full minutes fit inside 125 seconds. "
            "<code>125 % 60</code> is <code>5</code> — five seconds are left over. Used together, "
            "they split any total into clean chunks.</p>"
        ),
        "challenge_html": (
            "Fix <strong>minutes</strong> to use <code>//</code> and <strong>seconds</strong> to "
            "use <code>%</code> on <strong>total_seconds</strong>, then hit Run. Output should "
            "read <strong>2m 5s</strong>, not <strong>125m 125s</strong>."
        ),
        "starter_code": (
            "total_seconds = 125\n\n"
            "minutes = total_seconds  # use // here\n"
            "seconds = total_seconds  # use % here\n\n"
            'print(f"{minutes}m {seconds}s")'
        ),
        "check_pattern": r"(\d+m\s*\d+s)",
        "placeholder_value": "125m 125s",
        "success_message": "You split seconds into minutes and leftover seconds.",
    },
    {
        "slug": "string-formatting",
        "title": "String Formatting",
        "subtitle": "f-strings, Properly",
        "topic": "Basics",
        "order": 7,
        "xp": 50,
        "story_html": (
            "<p>Computers store decimals imperfectly. Multiply <code>19.9 * 3</code> and Python "
            "hands back <code>59.699999999999996</code> — the number is basically right, but it's "
            "ugly and wrong to actually show someone.</p>"
            "<p>Inside an f-string you can add a format spec after a colon. "
            "<code>{total:.2f}</code> means \"show this as a fixed-point number with exactly 2 "
            "decimal places.\" It rounds cleanly to <code>59.70</code> instead of dumping the raw mess.</p>"
        ),
        "challenge_html": (
            "Add <strong>:.2f</strong> inside the <strong>{total}</strong> in the f-string below, "
            "then hit Run. Output should read <strong>Total: $59.70</strong>, not a long decimal."
        ),
        "starter_code": (
            "price = 19.9\n"
            "quantity = 3\n"
            "total = price * quantity\n\n"
            '# fix the line below - add :.2f inside the {total}\n'
            'print(f"Total: ${total}")'
        ),
        "check_pattern": r"Total:\s*\$(\d+\.\d{2})\b",
        "placeholder_value": "",
        "success_message": "You formatted a float cleanly to 2 decimal places.",
    },
        {
        "slug": "if-statements",
        "title": "If Statements",
        "subtitle": "Just the Yes Branch",
        "topic": "Logic",
        "order": 8,
        "xp": 50,
        "story_html": (
            "<p>An <code>if</code> statement is a vibe check for your code: it looks at "
            "something, decides yes or no, and only runs the indented block underneath "
            "when it's <code>True</code>.</p>"
            "<p>If the condition is <code>False</code>, Python just... skips the block "
            "entirely. No error, no output, nothing — it moves straight on to whatever "
            "comes after. That's it. That's the whole idea, on its own, before anything "
            "else gets added to it.</p>"
        ),
        "challenge_html": (
            "<strong>is_weekend</strong> is <strong>False</strong>, so <strong>plan</strong> "
            "never gets overridden. Change it to <strong>True</strong>, then hit Run. "
            "Output should read <strong>Plan: sleep in</strong>, not <strong>Plan: go to class</strong>."
        ),
        "starter_code": (
            "is_weekend = False  # try changing to True\n\n"
            'plan = "go to class"\n\n'
            "if is_weekend:\n"
            '    plan = "sleep in"\n\n'
            'print(f"Plan: {plan}")'
        ),
        "check_pattern": r"Plan:\s*(.+)",
        "placeholder_value": "go to class",
        "success_message": "Your first if actually did something.",
    },
   {
        "slug": "conditionals",
        "title": "If / Else",
        "subtitle": "Two Roads, One Choice",
        "topic": "Logic",
        "order": 9,
        "xp": 50,
        "story_html": (
            "<p>You just saw <code>if</code> run a block only when something's true, and "
            "otherwise do nothing at all. Most of the time \"do nothing\" isn't good enough — "
            "you want something to happen either way.</p>"
            "<p>That's what <code>else</code> is for: the catch-all block that runs "
            "whenever the <code>if</code> didn't. Together, <code>if</code> / <code>else</code> "
            "always cover exactly two outcomes — one or the other, never both, never neither.</p>"
        ),
        "challenge_html": (
            "The <strong>else</strong> branch is currently just <strong>\"...\"</strong>. "
            "Give it a real plan, then hit Run. Output should read <strong>Plan: "
            "&lt;something real&gt;</strong>, not the dots."
        ),
        "starter_code": (
            "is_raining = False  # try switching to True\n\n"
            "if is_raining:\n"
            '    plan = "bring an umbrella"\n'
            "else:\n"
            '    plan = "..."  # fix me\n\n'
            'print(f"Plan: {plan}")'
        ),
        "check_pattern": r"Plan:\s*(.+)",
        "placeholder_value": "...",
        "success_message": "You covered both sides of the decision.",
    },
        {
        "slug": "elif",
        "title": "Elif",
        "subtitle": "More Than Two Choices",
        "topic": "Logic",
        "order": 10,
        "xp": 50,
        "story_html": (
            "<p>You just handled two outcomes with <code>if</code> / <code>else</code>. "
            "But real decisions rarely stop at two options. That's what <code>elif</code> "
            "is for — short for \"else if.\" Stack as many as you need in between "
            "<code>if</code> and <code>else</code> to check more cases, one at a time.</p>"
            "<p>Python checks each condition top to bottom and runs the <em>first</em> "
            "one that matches, then stops — it never checks the rest, even if they'd "
            "also be true. <code>else</code> still catches whatever's left over.</p>"
        ),
        "challenge_html": (
            "The <strong>sleepy</strong> branch is currently just <strong>\"...\"</strong> — "
            "not exactly a vibe. Give it a real value, then hit Run. Output should read "
            "<strong>Vibe check: &lt;something real&gt;</strong>, not the dots."
        ),
        "starter_code": (
            'mood = "sleepy"  # try: "hyped", "sleepy", or anything else\n\n'
            'if mood == "hyped":\n'
            '    vibe = "let\'s gooo"\n'
            'elif mood == "sleepy":\n'
            '    vibe = "..."  # fix me\n'
            'else:\n'
            '    vibe = "vibing"\n\n'
            'print(f"Vibe check: {vibe}")'
        ),
        "check_pattern": r"Vibe check:\s*(.+)",
        "placeholder_value": "...",
        "success_message": "Your code can finally read the room.",
    },
    {
        "slug": "loops-while",
        "title": "While Loops",
        "subtitle": "Until Something Changes",
        "topic": "Logic",
        "order": 11,
        "xp": 50,
        "story_html": (
            "<p>A <code>for</code> loop runs a set number of times. A <code>while</code> "
            "loop runs for as long as a condition stays <code>True</code> — it doesn't "
            "know in advance how many times that'll be, it just keeps checking before "
            "every pass.</p>"
            "<p>That means something inside the loop has to actually change the "
            "condition eventually, or it never stops. Forget to update it and you've "
            "written an infinite loop — one of the most common beginner bugs there is.</p>"
        ),
        "challenge_html": (
            "<strong>energy</strong> starts at 3. Change it to a different number, "
            "then hit Run — the first line should say <strong>energy: &lt;your number&gt;</strong>, "
            "not <strong>energy: 3</strong>."
        ),
        "starter_code": (
            "energy = 3  # change me - try a different starting number\n\n"
            "while energy > 0:\n"
            '    print(f"energy: {energy}")\n'
            "    energy -= 1\n\n"
            'print("done!")'
        ),
        "check_pattern": r"energy:\s*(\d+)",
        "placeholder_value": "3",
        "success_message": "You ran a loop that stops because you told it to.",
    },

    {
        "slug": "loops-for",
        "title": "For Loops",
        "subtitle": "Doing It Again, on Purpose",
        "topic": "Logic",
        "order": 12,
        "xp": 50,
        "story_html": (
            "<p>A <code>for</code> loop just means \"do this once per thing in here.\" "
            "<code>for i in range(3):</code> runs its block 3 times, handing you "
            "<code>i = 0</code>, then <code>1</code>, then <code>2</code> — Python counts "
            "from zero, which trips everyone up at least once.</p>"
            "<p>Copy-pasting the same <code>print()</code> five times works, technically. "
            "A loop is just that, minus the copy-pasting — and it still works whether "
            "it's 5 reps or 5,000.</p>"
        ),
        "challenge_html": (
            "<strong>reps</strong> is stuck at 3. Change it to a different number, "
            "then hit Run — the last line should say <strong>rep &lt;your number&gt;: "
            "let's go!</strong> instead of always stopping at rep 3."
        ),
        "starter_code": (
            "reps = 3  # change me - how many times should this repeat?\n\n"
            "for i in range(reps):\n"
            '    print(f"rep {i+1}: let\'s go!")'
        ),
        "check_pattern": r"rep (\d+): let's go!\s*$",
        "placeholder_value": "3",
        "success_message": "You made your code repeat itself on purpose, for once.",
    },
    {
        "slug": "error-handling",
        "title": "Error Handling",
        "subtitle": "Try, Except, Survive",
        "topic": "Logic",
        "order": 13,
        "xp": 50,
        "story_html": (
            "<p>Some code can fail — turning <code>\"abc\"</code> into a number, for "
            "instance, just doesn't work. Left alone, that crashes your whole program.</p>"
            "<p><code>try</code> wraps the risky part. If it fails, Python jumps straight "
            "to <code>except</code> instead of crashing — you catch the problem and decide "
            "what happens next, instead of the program just dying mid-run.</p>"
        ),
        "challenge_html": (
            "<strong>age_text</strong> is <strong>\"abc\"</strong>, which isn't a number — "
            "so it's landing in the <strong>except</strong> block right now. Change it to "
            "a real number like <strong>\"25\"</strong>, then hit Run. Output should read "
            "<strong>Age: &lt;your number&gt;</strong>, not the error message."
        ),
        "starter_code": (
            'age_text = "abc"  # change me - try a real number like "25"\n\n'
            "try:\n"
            "    age = int(age_text)\n"
            '    print(f"Age: {age}")\n'
            "except ValueError:\n"
            '    print("That\'s not a number!")'
        ),
        "check_pattern": r"Age:\s*(\d+)",
        "placeholder_value": "",
        "success_message": "You caught a crash before it happened.",
    },
    {
    "slug": "lists-creating",
    "title": "Lists",
    "subtitle": "The Party Roster",
    "topic": "Collections",
    "order": 14,
    "xp": 50,
    "story_html": (
        "<p>A variable holds one thing. A <code>list</code> holds many things, in order, "
        "under one name. Think of it as your party roster — one box, several recruits "
        "lined up inside it.</p>"
        "<p><code>party = [\"Kael\", \"Rin\", \"Bo\"]</code> creates a roster of three. "
        "Each recruit has a position — Python calls it an <strong>index</strong> — starting "
        "from <code>0</code>, not <code>1</code>. So <code>party[0]</code> is Kael, the "
        "front-liner, and <code>party[2]</code> is Bo, third in line.</p>"
        "<p>Negative indexes count backward from the end: <code>party[-1]</code> is always "
        "the <em>last</em> recruit, no matter how long the roster gets — handy when you "
        "don't want to count.</p>"
    ),
    "challenge_html": (
        "Right now the spell always calls out the <strong>first</strong> recruit. Change "
        "the index so it calls out the <strong>last</strong> one instead — without counting "
        "the list by hand. Output should read <strong>Front-liner: Bo</strong>."
    ),
    "starter_code": (
        'party = ["Kael", "Rin", "Bo"]\n\n'
        "front_liner = party[0]  # fix me - grab the LAST recruit, not the first\n\n"
        'print(f"Front-liner: {front_liner}")'
    ),
    "check_pattern": r"Front-liner:\s*(.+)",
    "placeholder_value": "Kael",
    "success_message": "You indexed a list without counting a single element by hand.",
},
{
    "slug": "list-methods",
    "title": "List Methods",
    "subtitle": "Managing the Roster",
    "topic": "Collections",
    "order": 15,
    "xp": 50,
    "story_html": (
        "<p>A roster isn't static — people join, people leave, people get reordered. "
        "Lists come with built-in moves for exactly that.</p>"
        "<p><code>.append(x)</code> recruits <code>x</code> onto the end. "
        "<code>.remove(x)</code> dismisses the first recruit matching <code>x</code>. "
        "<code>.sort()</code> reorders the whole list in place — alphabetically for text, "
        "smallest-to-largest for numbers.</p>"
        "<p>These change the list itself, not a copy — call <code>.append()</code> and the "
        "original <code>party</code> is different from that point on.</p>"
    ),
    "challenge_html": (
        "<strong>\"Bo\"</strong> rage-quit the party but is still on the roster, and "
        "<strong>\"Nix\"</strong> just joined but hasn't been added. Remove Bo, append Nix, "
        "then hit Run. Output should read <strong>Roster: ['Kael', 'Rin', 'Nix']</strong>."
    ),
    "starter_code": (
        'party = ["Kael", "Rin", "Bo"]\n\n'
        "# fix me - remove \"Bo\", then append \"Nix\"\n\n"
        'print(f"Roster: {party}")'
    ),
    "check_pattern": r"Roster:\s*(\[.+?\])",
    "placeholder_value": "['Kael', 'Rin', 'Bo']",
    "success_message": "You managed a roster with append and remove.",
},
{
    "slug": "loops-lists",
    "title": "Looping Over Lists",
    "subtitle": "Calling the Whole Roster",
    "topic": "Collections",
    "order": 16,
    "xp": 50,
    "story_html": (
        "<p>You already know <code>for i in range(n)</code> repeats something <code>n</code> "
        "times. A <code>for</code> loop can also walk a list directly — no indexing needed: "
        "<code>for member in party:</code> hands you one recruit at a time, in order.</p>"
        "<p>When you need the <em>position</em> too — \"recruit #2 is Rin\" — wrap the list "
        "in <code>enumerate()</code>: <code>for i, member in enumerate(party):</code> gives "
        "you both the index and the value on every pass, together.</p>"
    ),
    "challenge_html": (
        "The loop below is only printing names, no numbers. Switch it to use "
        "<code>enumerate()</code> so each line reads <strong>Recruit "
        "&lt;number&gt;: &lt;name&gt;</strong>, starting from <strong>1</strong>, not 0."
    ),
    "starter_code": (
        'party = ["Kael", "Rin", "Bo"]\n\n'
        "for member in party:  # fix me - use enumerate() and start counting at 1\n"
        '    print(f"Recruit: {member}")'
    ),
    "check_pattern": r"Recruit 1:\s*(.+)",
    "placeholder_value": "",
    "success_message": "You looped a list while tracking position with enumerate.",
},
{
    "slug": "list-slicing",
    "title": "Slicing",
    "subtitle": "Sending In a Squad",
    "topic": "Collections",
    "order": 17,
    "xp": 50,
    "story_html": (
        "<p>Sometimes you don't want one recruit or the whole roster — just a chunk of it. "
        "That's slicing: <code>party[start:end]</code> grabs everything from "
        "<code>start</code> up to, but <em>not including</em>, <code>end</code>.</p>"
        "<p><code>party[1:3]</code> on a 4-person roster grabs recruits at index "
        "<code>1</code> and <code>2</code> — the middle two, skipping the front-liner and "
        "the back-liner. Leave off a side and Python fills in the rest: <code>party[:2]</code> "
        "is \"from the start up to 2,\" <code>party[2:]</code> is \"from 2 to the end.\"</p>"
    ),
    "challenge_html": (
        "Send in the <strong>middle two</strong> recruits — not the first, not the last. "
        "Fix the slice, then hit Run. Output should read "
        "<strong>Squad: ['Rin', 'Bo']</strong>."
    ),
    "starter_code": (
        'party = ["Kael", "Rin", "Bo", "Nix"]\n\n'
        "squad = party[0:1]  # fix me - grab just the middle two\n\n"
        'print(f"Squad: {squad}")'
    ),
    "check_pattern": r"Squad:\s*(\[.+?\])",
    "placeholder_value": "['Kael']",
    "success_message": "You sliced a list to grab exactly the chunk you needed.",
},
{
    "slug": "dicts-creating",
    "title": "Dictionaries",
    "subtitle": "The Character Sheet",
    "topic": "Collections",
    "order": 18,
    "xp": 50,
    "story_html": (
        "<p>A list finds things by position — <code>party[0]</code>, <code>party[1]</code>. "
        "A <code>dict</code> finds things by <strong>name</strong> instead. Think of it as a "
        "character sheet: no one remembers stat #2, they remember \"HP.\"</p>"
        "<p><code>hero = {\"name\": \"Kael\", \"hp\": 40}</code> creates two named slots — "
        "<strong>keys</strong> (<code>\"name\"</code>, <code>\"hp\"</code>) each pointing at a "
        "<strong>value</strong>. Grab a value with <code>hero[\"hp\"]</code>, same bracket "
        "syntax as a list, just with a name instead of a number.</p>"
        "<p>Ask for a key that doesn't exist — <code>hero[\"mana\"]</code> when there's no "
        "<code>\"mana\"</code> slot — and Python crashes with a <code>KeyError</code>. Unlike "
        "a list running out of positions, this one's easy to hit by a typo alone.</p>"
    ),
    "challenge_html": (
        "The sheet only tracks <strong>hp</strong> right now, but the print line is asking "
        "for <strong>mp</strong> too. Add an <strong>\"mp\"</strong> key to <strong>hero</strong>, "
        "then hit Run. Output should read <strong>HP: 40 | MP: 15</strong>, not a crash."
    ),
    "starter_code": (
        'hero = {"name": "Kael", "hp": 40}  # fix me - add an "mp" key worth 15\n\n'
        'print(f"HP: {hero[\"hp\"]} | MP: {hero[\"mp\"]}")'
    ),
    "check_pattern": r"HP:\s*\d+\s*\|\s*MP:\s*(\d+)",
    "placeholder_value": "",
    "success_message": "You built a character sheet and read it back by name, not position.",
},
{
    "slug": "dict-methods",
    "title": "Dictionary Methods",
    "subtitle": "Reading the Sheet Safely",
    "topic": "Collections",
    "order": 19,
    "xp": 50,
    "story_html": (
        "<p>Grabbing a missing key with <code>[ ]</code> crashes your program. "
        "<code>.get(\"key\")</code> asks the same question but hands back <code>None</code> "
        "instead of crashing if it's missing — and <code>.get(\"key\", default)</code> lets "
        "you name your own fallback instead of <code>None</code>.</p>"
        "<p>Three more worth knowing: <code>.keys()</code> lists every stat name on the "
        "sheet, <code>.values()</code> lists every stat value, and <code>.items()</code> "
        "gives you both, paired together — that last one is what you'll reach for most.</p>"
    ),
    "challenge_html": (
        "<strong>hero</strong> has no <strong>\"level\"</strong> stat, and reading it "
        "directly would crash. Use <code>.get()</code> with a default of "
        "<strong>1</strong> instead, then hit Run. Output should read "
        "<strong>Level: 1</strong>, not a crash."
    ),
    "starter_code": (
        'hero = {"name": "Kael", "hp": 40}\n\n'
        'level = hero["level"]  # fix me - use .get() with a default of 1 instead\n\n'
        'print(f"Level: {level}")'
    ),
    "check_pattern": r"Level:\s*(\d+)",
    "placeholder_value": "",
    "success_message": "You read a missing stat safely instead of crashing on it.",
},
{
    "slug": "loops-dicts",
    "title": "Looping Over Dictionaries",
    "subtitle": "Printing the Full Sheet",
    "topic": "Collections",
    "order": 20,
    "xp": 50,
    "story_html": (
        "<p>Looping a list hands you one value per pass. Looping a dict with just "
        "<code>for stat in hero:</code> only hands you the <em>keys</em> — you'd still have "
        "to look up each value yourself.</p>"
        "<p><code>.items()</code> fixes that: <code>for stat, value in hero.items():</code> "
        "hands you both the key and the value together, every pass — same shape as looping "
        "a list with <code>enumerate()</code>, just for named slots instead of numbered ones.</p>"
    ),
    "challenge_html": (
        "The loop below is only printing stat names, not their values. Switch it to unpack "
        "both with <code>.items()</code> so each line reads <strong>&lt;stat&gt;: "
        "&lt;value&gt;</strong>, for every stat on the sheet."
    ),
    "starter_code": (
        'hero = {"hp": 40, "mp": 15, "level": 3}\n\n'
        "for stat in hero:  # fix me - use .items() to get the value too\n"
        '    print(f"{stat}")'
    ),
    "check_pattern": r"hp:\s*(\d+)",
    "placeholder_value": "",
    "success_message": "You printed a full character sheet, stat and value together.",
},
{
    "slug": "dicts-updating-nesting",
    "title": "Updating & Nesting",
    "subtitle": "Changing the Sheet Mid-Fight",
    "topic": "Collections",
    "order": 21,
    "xp": 50,
    "story_html": (
        "<p>Stats don't stay the same forever — a hero heals, levels up, picks up gear. "
        "Changing a value in a dict works just like setting a variable: "
        "<code>hero[\"hp\"] = 50</code> overwrites whatever was there before. If the key "
        "doesn't exist yet, this same line <em>creates</em> it — no separate step needed.</p>"
        "<p>A dict's values don't have to be plain numbers or text either. They can be a "
        "list. <code>hero[\"inventory\"] = [\"sword\", \"shield\"]</code> gives your hero a "
        "bag of items, stored right on their own sheet. You reach into it the same way you "
        "always would: <code>hero[\"inventory\"][0]</code> is the first item, "
        "<code>\"sword\"</code>.</p>"
    ),
    "challenge_html": (
        "Kael just got healed to full and picked up a potion. Update "
        "<strong>hp</strong> to <strong>50</strong>, and add <strong>\"potion\"</strong> to "
        "the <strong>inventory</strong> list using <code>.append()</code>, then hit Run. "
        "Output should read <strong>HP: 50 | Bag: ['sword', 'potion']</strong>."
    ),
    "starter_code": (
        'hero = {"hp": 30, "inventory": ["sword"]}\n\n'
        "# fix me - update hp to 50\n"
        "# fix me - append \"potion\" to hero[\"inventory\"]\n\n"
        'print(f"HP: {hero["hp"]} | Bag: {hero["inventory"]}")'
    ),
    "check_pattern": r"HP:\s*50\s*\|\s*Bag:\s*(\[.+?\])",
    "placeholder_value": "",
    "success_message": "You updated a stat and grew a list living inside a dict.",
},
{
    "slug": "tuples",
    "title": "Tuples",
    "subtitle": "The Locked Loadout",
    "topic": "Collections",
    "order": 22,
    "xp": 50,
    "story_html": (
        "<p>A list can change any time — append, remove, sort. A <code>tuple</code> looks "
        "almost identical but can't: once it's made, it's locked. Think of it as a loadout "
        "you commit to before a fight, not a bag you keep digging through mid-battle.</p>"
        "<p>You write a tuple with parentheses instead of brackets: "
        "<code>loadout = (\"sword\", \"shield\")</code>. Reading it works exactly like a "
        "list — <code>loadout[0]</code> is <code>\"sword\"</code> — but try "
        "<code>loadout[0] = \"axe\"</code> and Python refuses with a "
        "<code>TypeError</code>. That's not a bug, it's the entire point of a tuple: "
        "some data should be locked once it's set.</p>"
    ),
    "challenge_html": (
        "The starter code tries to swap <strong>\"shield\"</strong> for "
        "<strong>\"axe\"</strong> by editing the tuple directly — that will crash. "
        "Instead, build a brand-new tuple called <strong>loadout</strong> that already "
        "has <strong>\"axe\"</strong> in it, then hit Run. Output should read "
        "<strong>Loadout: ('sword', 'axe')</strong>."
    ),
    "starter_code": (
        'loadout = ("sword", "shield")\n\n'
        '# fix me - loadout[1] = "axe" crashes. Instead, make a new tuple\n'
        '# called loadout that holds ("sword", "axe")\n\n'
        'print(f"Loadout: {loadout}")'
    ),
    "check_pattern": r"Loadout:\s*(\(.+?\))",
    "placeholder_value": "('sword', 'shield')",
    "success_message": "You worked with a tuple by respecting that it can't be edited in place.",
},
{
    "slug": "sets",
    "title": "Sets",
    "subtitle": "The Loot Pool",
    "topic": "Collections",
    "order": 23,
    "xp": 50,
    "story_html": (
        "<p>A list can hold the same item twice. Sometimes that's wrong — a loot pool "
        "shouldn't list <code>\"gold coin\"</code> five times just because five drops "
        "happened to be the same. A <code>set</code> fixes that automatically: it can "
        "only ever hold each value <em>once</em>, no duplicates allowed.</p>"
        "<p>Write one with curly braces: <code>loot = {\"sword\", \"gold\", \"gold\"}</code> "
        "quietly collapses down to just two items — Python drops the repeat for you, "
        "no error, no warning. A set also doesn't keep order the way a list does; it "
        "just guarantees uniqueness.</p>"
        "<p><code>.add(x)</code> throws something into the pool. If it's already in "
        "there, nothing happens — no error, no second copy.</p>"
    ),
    "challenge_html": (
        "Two <strong>\"gold\"</strong> drops and one <strong>\"gem\"</strong> just landed "
        "in the pool. Add all three drops using <code>.add()</code>, then hit Run. Output "
        "should show <strong>3</strong> unique items in the pool, not 1."
    ),
    "starter_code": (
        'loot = {"sword"}\n\n'
        '# fix me - .add() "gold", "gold" again, and "gem"\n\n'
        'print(f"Unique drops: {len(loot)}")'
    ),
    "check_pattern": r"Unique drops:\s*(\d+)",
    "placeholder_value": "1",
    "success_message": "You built a loot pool that dedupes itself automatically.",
},
{
    "slug": "membership-choosing",
    "title": "Membership & Choosing the Right One",
    "subtitle": "Is It In There?",
    "topic": "Collections",
    "order": 24,
    "xp": 50,
    "story_html": (
        "<p>Every collection you've met — list, dict, tuple, set — answers the same "
        "question the same way: <code>x in collection</code> returns <code>True</code> "
        "or <code>False</code> depending on whether <code>x</code> is inside it. For a "
        "dict, <code>in</code> checks the <strong>keys</strong>, not the values.</p>"
        "<p>Sets are built for this check specifically — searching a set for membership "
        "is fast even when it's huge, which is a big part of why they exist. So: use a "
        "<strong>list</strong> when order matters and duplicates are fine, a "
        "<strong>set</strong> when you only care what's present, a "
        "<strong>tuple</strong> when the data shouldn't change, and a "
        "<strong>dict</strong> when every value needs its own name.</p>"
    ),
    "challenge_html": (
        "<strong>banned_items</strong> is a set. Right now the code always prints "
        "\"allowed\" no matter what. Use <code>in</code> to actually check if "
        "<strong>item</strong> is inside <strong>banned_items</strong>, then hit Run. "
        "Output should read <strong>cursed ring: blocked</strong>."
    ),
    "starter_code": (
        'banned_items = {"cursed ring", "poison vial"}\n'
        'item = "cursed ring"\n\n'
        'status = "allowed"  # fix me - check if item is in banned_items\n\n'
        'print(f"{item}: {status}")'
    ),
    "check_pattern": r"cursed ring:\s*(blocked|allowed)",
    "placeholder_value": "allowed",
    "success_message": "You checked membership and picked the right tool for the job.",
},
{
    "slug": "list-comprehensions",
    "title": "List Comprehensions",
    "subtitle": "Loops in One Line",
    "topic": "Collections",
    "order": 25,
    "xp": 50,
    "story_html": (
        "<p>You've written loops like this before: start an empty list, loop over "
        "something, append to the list each time. It works — but it's three lines to "
        "say one idea: \"make a new list out of an old one.\"</p>"
        "<p>A list comprehension says the same thing in one line: "
        "<code>[x * 2 for x in numbers]</code> reads almost like English — \"give me "
        "<code>x * 2</code>, for every <code>x</code> in <code>numbers</code>.\" It "
        "builds a brand-new list, leaving the original untouched.</p>"
        "<p>This isn't a new concept — it's a shortcut for a loop you already know how "
        "to write. If the one-liner ever looks confusing, you can always mentally "
        "expand it back into the loop form first.</p>"
    ),
    "challenge_html": (
        "The loop below builds <strong>doubled</strong> the long way. Rewrite it as a "
        "single-line list comprehension instead, then hit Run. Output should still read "
        "<strong>Doubled: [2, 4, 6, 8]</strong>."
    ),
    "starter_code": (
        "numbers = [1, 2, 3, 4]\n\n"
        "# fix me - build doubled using a list comprehension:\n"
        "# doubled = [n * 2 for n in numbers]\n\n"
        'print(f"Doubled: {doubled}")'
    ),
    "check_pattern": r"Doubled:\s*(\[.+?\])",
    "placeholder_value": "",
    "success_message": "You rewrote a loop as a one-line list comprehension.",
},
{
    "slug": "list-comprehensions-filtering",
    "title": "Comprehensions with a Filter",
    "subtitle": "Only the Ones That Count",
    "topic": "Collections",
    "order": 26,
    "xp": 50,
    "story_html": (
        "<p>A comprehension can also filter as it builds — skip the ones you don't "
        "want, keep the ones you do, all in the same line. Tack an <code>if</code> on "
        "the end: <code>[x for x in party if x != \"Bo\"]</code> builds a new list with "
        "every party member <em>except</em> Bo.</p>"
        "<p>The pattern is always: <code>[expression for item in collection if "
        "condition]</code>. Read it left to right as \"give me <em>expression</em>, for "
        "every <em>item</em> in <em>collection</em>, but only when <em>condition</em> is "
        "true.\" Anything that fails the condition just doesn't make it into the new list.</p>"
    ),
    "challenge_html": (
        "<strong>survivors</strong> should only include party members with "
        "<strong>hp > 0</strong>, but right now it's copying everyone. Add the missing "
        "<code>if</code> filter, then hit Run. Output should read "
        "<strong>Survivors: ['Kael', 'Rin']</strong>, not all three."
    ),
    "starter_code": (
        'party_hp = {"Kael": 40, "Rin": 15, "Bo": 0}\n\n'
        "survivors = [name for name in party_hp]  # fix me - add: if party_hp[name] > 0\n\n"
        'print(f"Survivors: {survivors}")'
    ),
    "check_pattern": r"Survivors:\s*(\[.+?\])",
    "placeholder_value": "['Kael', 'Rin', 'Bo']",
    "success_message": "You filtered a list down to only what matters, in one line.",
},
{
    "slug": "functions",
    "title": "Functions",
    "subtitle": "Reusable Spells",
    "topic": "Functions",
    "order": 27,
    "xp": 50,
    "story_html": (
        "<p>You've been reusing Python's built-in spells this whole time — "
        "<code>print()</code>, <code>len()</code>. A function lets you write your own.</p>"
        "<p><code>def greet():</code> starts a new spell named <code>greet</code>. "
        "Everything indented underneath is the spell's recipe — it doesn't run yet, it "
        "just gets <em>saved</em>. To actually cast it, you call it by name with "
        "parentheses: <code>greet()</code>. Write the recipe once, cast it as many "
        "times as you want, no copy-pasting.</p>"
    ),
    "challenge_html": (
        "The <strong>greet</strong> spell is defined but never actually cast. Call it "
        "twice, then hit Run. Output should read <strong>Welcome, traveler!</strong> "
        "on two separate lines."
    ),
    "starter_code": (
        "def greet():\n"
        '    print("Welcome, traveler!")\n\n'
        "# fix me - call greet() twice below\n"
    ),
    "check_pattern": r"(Welcome, traveler!\s*\n\s*Welcome, traveler!)",
    "placeholder_value": "",
    "success_message": "You defined a spell once and cast it more than once.",
},
{
    "slug": "function-args",
    "title": "Arguments & Returns",
    "subtitle": "Passing Stuff In and Out",
    "topic": "Functions",
    "order": 28,
    "xp": 50,
    "story_html": (
        "<p>A spell that always does the exact same thing isn't that useful. "
        "<strong>Parameters</strong> let you pass something different in each time: "
        "<code>def greet(name):</code> expects one ingredient, and "
        "<code>greet(\"Kael\")</code> hands <code>\"Kael\"</code> in as <code>name</code> "
        "for that one cast.</p>"
        "<p><code>print()</code> inside a function shows something on screen — but it "
        "doesn't hand anything back to whoever called it. <code>return</code> does: "
        "<code>def double(n): return n * 2</code> lets you write <code>result = "
        "double(5)</code> and actually store the answer, <code>10</code>, in a variable "
        "to use later.</p>"
    ),
    "challenge_html": (
        "<strong>heal</strong> takes an <strong>hp</strong> and an <strong>amount</strong>, "
        "but right now it doesn't send anything back — it just calculates and forgets. "
        "Add a <code>return</code> so the healed total actually comes out, then hit Run. "
        "Output should read <strong>New HP: 45</strong>."
    ),
    "starter_code": (
        "def heal(hp, amount):\n"
        "    new_hp = hp + amount\n"
        "    # fix me - return new_hp\n\n"
        "result = heal(30, 15)\n"
        'print(f"New HP: {result}")'
    ),
    "check_pattern": r"New HP:\s*(\d+)",
    "placeholder_value": "",
    "success_message": "You passed values in and got a real answer back out.",
},
{
    "slug": "modules",
    "title": "Modules & Imports",
    "subtitle": "Borrowing Other People's Code",
    "topic": "Structure",
    "order": 29,
    "xp": 50,
    "story_html": (
        "<p>You don't have to write every spell from scratch — Python ships with whole "
        "spellbooks, called <strong>modules</strong>, already written. "
        "<code>import random</code> unlocks everything inside the <code>random</code> "
        "module, and you reach into it with a dot: <code>random.randint(1, 6)</code> "
        "rolls a die between 1 and 6.</p>"
        "<p>If you only need one specific spell out of a whole module, "
        "<code>from random import randint</code> pulls in just that one — then you call "
        "it directly as <code>randint(1, 6)</code>, no <code>random.</code> prefix needed.</p>"
    ),
    "challenge_html": (
        "This code tries to use <strong>randint</strong> without importing it — that "
        "will crash. Add the missing import at the top, then hit Run. Output should "
        "read <strong>Roll: &lt;some number 1-6&gt;</strong>, not an error."
    ),
    "starter_code": (
        "# fix me - import randint from the random module\n\n"
        "roll = randint(1, 6)\n"
        'print(f"Roll: {roll}")'
    ),
    "check_pattern": r"Roll:\s*([1-6])\b",
    "placeholder_value": "",
    "success_message": "You borrowed a ready-made spell from Python's standard library.",
},
{
    "slug": "file-basics",
    "title": "File Basics",
    "subtitle": "Reading & Writing Scrolls",
    "topic": "Structure",
    "order": 30,
    "xp": 50,
    "story_html": (
        "<p>Everything you've built so far disappears the moment the program ends. "
        "Files are how you make something stick around — a scroll instead of a "
        "spoken spell.</p>"
        "<p><code>with open(\"log.txt\", \"w\") as f:</code> opens a scroll for "
        "<strong>w</strong>riting. Inside that block, <code>f.write(\"hello\")</code> "
        "puts text on it. The <code>with</code> part matters: it automatically closes "
        "the file when you're done, even if something goes wrong partway through — you "
        "don't have to remember to close it yourself.</p>"
        "<p>To read a scroll back, swap the mode: <code>with open(\"log.txt\", \"r\") "
        "as f:</code> then <code>f.read()</code> hands you everything that's on it, as "
        "one big string.</p>"
    ),
    "challenge_html": (
        "This code opens <strong>quest.txt</strong> to read it, but nothing was ever "
        "written to it first. Add a write step before the read, saving the text "
        "<strong>\"Slay the dragon\"</strong>, then hit Run. Output should read "
        "<strong>Quest: Slay the dragon</strong>."
    ),
    "starter_code": (
        "# fix me - open quest.txt in \"w\" mode and write \"Slay the dragon\" to it\n\n"
        'with open("quest.txt", "r") as f:\n'
        "    contents = f.read()\n\n"
        'print(f"Quest: {contents}")'
    ),
    "check_pattern": r"Quest:\s*(Slay the dragon)",
    "placeholder_value": "",
    "success_message": "You wrote a file and read it back.",
},
{
    "slug": "classes-intro",
    "title": "Classes",
    "subtitle": "Blueprints for Heroes",
    "topic": "OOP",
    "order": 31,
    "xp": 50,
    "story_html": (
        "<p>A dict can hold one hero's stats. But if you want to make ten heroes, "
        "each with the same <em>shape</em> — a name, an hp, a level — retyping that "
        "dict ten times gets old fast. A <code>class</code> is a blueprint: define the "
        "shape once, stamp out as many heroes as you want from it.</p>"
        "<p><code>class Hero:</code> starts the blueprint. Inside it, "
        "<code>def __init__(self, name, hp):</code> is the setup step that runs every "
        "time a new hero gets made — <code>self.name = name</code> saves the name onto "
        "<em>this specific hero</em>. <code>self</code> just means \"the hero currently "
        "being built,\" so each one keeps its own separate stats.</p>"
        "<p>To actually make a hero from the blueprint: <code>kael = Hero(\"Kael\", "
        "40)</code>. Then <code>kael.name</code> and <code>kael.hp</code> read back "
        "exactly what you'd expect.</p>"
    ),
    "challenge_html": (
        "The <strong>Hero</strong> blueprint only saves <strong>name</strong> right "
        "now — <strong>hp</strong> gets dropped. Fix <code>__init__</code> so it saves "
        "hp too, then hit Run. Output should read <strong>Kael has 40 HP</strong>."
    ),
    "starter_code": (
        "class Hero:\n"
        "    def __init__(self, name, hp):\n"
        "        self.name = name\n"
        "        # fix me - also save self.hp = hp\n\n"
        'kael = Hero("Kael", 40)\n'
        'print(f"{kael.name} has {kael.hp} HP")'
    ),
    "check_pattern": r"Kael has (\d+) HP",
    "placeholder_value": "",
    "success_message": "You built a class and stamped out your first object from it.",
},
{
    "slug": "objects-methods",
    "title": "Objects & Methods",
    "subtitle": "Giving Things Behavior",
    "topic": "OOP",
    "order": 32,
    "xp": 50,
    "story_html": (
        "<p>A blueprint that only stores stats is just a fancy dict. The real power of "
        "a class is giving it <strong>behavior</strong> — actions the hero can take on "
        "themselves.</p>"
        "<p>A <strong>method</strong> is a function defined inside a class: "
        "<code>def take_damage(self, amount): self.hp -= amount</code>. It always takes "
        "<code>self</code> first, so it knows which hero it's acting on. Call it with "
        "<code>kael.take_damage(10)</code> — no need to pass <code>self</code> "
        "yourself, Python fills that part in automatically.</p>"
        "<p>Every hero made from the same blueprint gets the same methods, but each "
        "call only affects <em>that one</em> hero's own stats — <code>kael.hp</code> "
        "and <code>rin.hp</code> stay completely independent.</p>"
    ),
    "challenge_html": (
        "<strong>take_damage</strong> is defined but never actually reduces hp — fix "
        "the method body, then hit Run. Output should read <strong>Kael has 25 HP</strong> "
        "after taking 15 damage from 40."
    ),
    "starter_code": (
        "class Hero:\n"
        "    def __init__(self, name, hp):\n"
        "        self.name = name\n"
        "        self.hp = hp\n\n"
        "    def take_damage(self, amount):\n"
        "        pass  # fix me - self.hp -= amount\n\n"
        'kael = Hero("Kael", 40)\n'
        "kael.take_damage(15)\n"
        'print(f"{kael.name} has {kael.hp} HP")'
    ),
    "check_pattern": r"Kael has (\d+) HP",
    "placeholder_value": "40",
    "success_message": "You gave your object a method that changes its own state.",
},
{
    "slug": "mini-project",
    "title": "Mini Project",
    "subtitle": "Putting It All Together",
    "topic": "Project",
    "order": 33,
    "xp": 100,
    "story_html": (
        "<p>Everything up to here has been one idea at a time. This is where it all "
        "combines: a class with its own stats and methods, a list of objects to loop "
        "over, and a function to tie the whole battle together.</p>"
        "<p>Nothing new to learn in this one — just your own tools, working together "
        "the way real programs actually use them.</p>"
    ),
    "challenge_html": (
        "The <strong>battle</strong> function should have every hero in "
        "<strong>party</strong> attack the <strong>boss</strong>, and print the boss's "
        "remaining hp after each hit. Right now the loop body is empty. Fill it in "
        "using <code>.take_damage()</code>, then hit Run. Final line should read "
        "<strong>Boss HP: 10</strong>."
    ),
    "starter_code": (
        "class Hero:\n"
        "    def __init__(self, name, attack):\n"
        "        self.name = name\n"
        "        self.attack = attack\n\n"
        "class Boss:\n"
        "    def __init__(self, hp):\n"
        "        self.hp = hp\n\n"
        "    def take_damage(self, amount):\n"
        "        self.hp -= amount\n\n"
        "def battle(party, boss):\n"
        "    for hero in party:\n"
        "        pass  # fix me - boss.take_damage(hero.attack), then print Boss HP\n\n"
        'party = [Hero("Kael", 20), Hero("Rin", 15), Hero("Bo", 15)]\n'
        "boss = Boss(60)\n"
        "battle(party, boss)"
    ),
    "check_pattern": r"Boss HP:\s*(\d+)",
    "placeholder_value": "",
    "success_message": "You built and ran a full battle system — classes, lists, and functions working together.",
},
]

LESSONS.sort(key=lambda l: l["order"])


def get_lesson(slug):
    return next((l for l in LESSONS if l["slug"] == slug), None)


def is_playable(lesson):
    return bool(lesson.get("starter_code"))


def next_slug(slug):
    """Slug of the lesson right after this one, or None if it's the last."""
    idx = next((i for i, l in enumerate(LESSONS) if l["slug"] == slug), None)
    if idx is None or idx + 1 >= len(LESSONS):
        return None
    return LESSONS[idx + 1]["slug"]

def continue_slug(completed_slugs):
    """
    Slug of the lesson a user should land on when they click a generic
    "continue" CTA (e.g. the homepage hero button): the very next lesson
    in path order they haven't finished - even if it's still a "coming
    soon" stub, since that's the honest state of the path. Falls back to
    the first lesson if everything is already completed.
    """
    for l in LESSONS:
        if l["slug"] not in completed_slugs:
            return l["slug"]
    return LESSONS[0]["slug"]
def is_unlocked(lesson, completed_slugs):
    """
    A lesson is unlocked once every *playable* lesson before it in path
    order has been completed. Lessons that are still "coming soon" don't
    block progress - only real, finishable lessons do, so the path never
    gets permanently stuck on unwritten content.
    """
    for l in LESSONS:
        if l["order"] >= lesson["order"]:
            break
        if is_playable(l) and l["slug"] not in completed_slugs:
            return False
    return True