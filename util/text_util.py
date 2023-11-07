def insert_line_breaks(text, max_length=50):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) > max_length:
            lines.append(current_line.strip())
            current_line = ""
        current_line += " " + word
    if current_line:
        lines.append(current_line.strip())
    return lines#"<br>".join(lines)
def wrap_labels(labels):
    wrapped_labels = []
    for label in labels:
        wrapped_labels.append(insert_line_breaks(label))
    return wrapped_labels
