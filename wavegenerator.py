import argparse
import csv
import numpy as np


def main():
    args = parse_args()
    points = read_points(args.points_file)
    points = interpolate_points(points, args.length)
    output_file = args.output or args.points_file
    write_points(points, output_file)


def parse_args():
    parser = argparse.ArgumentParser(description="Waveforms generator")
    parser.add_argument("points_file",
                        help="path to CSV file with main points")
    parser.add_argument("-l", "--length", help="length of result waveform",
                        type=int, required=True)
    parser.add_argument("-o", "--output", help=(
        "file for writing waveform (if not specified, input file will be "
        "rewritten)"))
    return parser.parse_args()


def read_points(filename):
    points = []
    with open(filename, "rt", newline="") as fin:
        reader = csv.reader(fin)
        for row in reader:
            points.append((int(row[0]), float(row[1])))
    return points


def interpolate_points(points, length):
    points = np.array(points)
    points[:, 0] -= 1
    xvals = np.arange(length)
    return np.float32(
        np.interp(xvals, points[:, 0], points[:, 1], left=0.0, right=0.0)
    )


def write_points(points, filename):
    with open(filename, "w", newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(["data length", len(points)])
        writer.writerow(["frequency", 1.0])
        writer.writerow(["amp", 2.0])
        writer.writerow(["offset", 0.0])
        writer.writerow(["phase", 0.0])
        for _ in range(7):
            writer.writerow([])
        writer.writerow(["xpos", "value"])

        for i, y in enumerate(points):
            writer.writerow([i + 1, y])


if __name__ == "__main__":
    main()
