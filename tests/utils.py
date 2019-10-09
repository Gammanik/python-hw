def trim_lines(lines):
    return '\n'.join([
        line.lstrip() for line in lines.split('\n')
    ])
