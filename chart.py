#!/usr/bin/env python3.6

import sys
from typing import Iterator

import pandas as pd
from pygal import Line
from pygal.style import Style


class GruvboxStyle(Style):
    """ A gruvbox-inspired Pygal style. """

    background = '#282828'
    plot_background = '#1d2021'
    foreground = '#fdf4c1'
    foreground_strong = '#fdf4c1'
    foreground_subtle = '#fdf4c1'
    colors = ('#8ec07c', '#fa5c4b')


def dilute_datetimes(datetimes: pd.Series, factor: int) -> Iterator[str]:
    """ Lots of datetimes overlap and become unreadable, make some space. """
    dilute = lambda t: t[1] if t[0] % factor == 0 else ''
    yield from map(dilute, enumerate(datetimes))


def generate_chart(data: pd.DataFrame) -> Line:
    line_chart = Line(
        js=(),  # The tooltips are really nice, but I don't want any JS.
        style=GruvboxStyle,
        x_label_rotation=30
    )

    # Water those datetimes down so they don't overlap and we can read them!
    datetimes = data['Datetime']
    dilution_factor = datetimes.shape[0] // 10
    datetimes = dilute_datetimes(datetimes, factor=dilution_factor)

    line_chart.title = 'HTTP GET by IP vs. HTTP GET by Hostname'
    line_chart.y_title = 'Seconds'
    line_chart.x_labels = datetimes
    line_chart.add(
        title='By IP',
        values=data['Seconds for HTTP GET by IP']
    )
    line_chart.add(
        title='By Hostname',
        values=data['Seconds for HTTP GET by Hostname']
    )
    return line_chart


def main(argv: list) -> None:
    data = pd.read_csv(sys.argv[1])
    output = sys.argv[2]
    chart = generate_chart(data)
    chart.render_to_file(output)


if __name__ == '__main__':
    main(sys.argv)
