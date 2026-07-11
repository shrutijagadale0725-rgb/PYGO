import importlib.util

spec = importlib.util.spec_from_file_location("lessons_check", "app/lessons.py")
lessons_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lessons_module)

for l in lessons_module.LESSONS:
    status = "OK" if lessons_module.is_playable(l) else "STUB"
    print(f'{l["order"]:2} {l["slug"]:24} {l["topic"]:12} {status}')