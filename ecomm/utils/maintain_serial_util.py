import inspect


def maintain_serial():
    frame = inspect.currentframe()
    caller_class = frame.f_back.f_locals.get('self').__class__
    print(f"name of the class: {caller_class}")
    last_entry = caller_class.objects.all().order_by('id').last()
    if last_entry:
        return last_entry.id + 1
    return last_entry
