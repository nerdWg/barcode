from svgwrite import Drawing


def create_image(code: str) -> Drawing:
    stroke_width = 5
    margin = 100
    image_width = len(code) * stroke_width + 2 * margin
    image_height = 500
    drawing = Drawing(
        size=(image_width, image_height),
        viewBox=f'0 0 {image_width} {image_height}'
    )
    foreground = 'black'
    background = 'white'
    shapes = drawing.add(drawing.g(id='shapes', fill=background))
    shapes.add(drawing.rect(insert=(0, 0), size=(image_width, image_height)))

    current_offset = margin
    for bit, run_length in runs(code):
        bar_width = stroke_width * run_length
        if bit == '1':
            shapes.add(drawing.rect(
                insert=(current_offset, margin),
                size=(bar_width, image_height - 2 * margin),
                fill=foreground
            ))
        current_offset += bar_width
    return drawing


def runs(code: str):
    current_runs = [[code[0], 1]]
    for bit in code[1:]:
        if bit == current_runs[-1][0]:
            current_runs[-1][1] += 1
        else:
            current_runs.append([bit, 1])
    return current_runs
