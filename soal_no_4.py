from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook

def parse_data(file_path):
    temp = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        timestamp = None
        for line in lines:
            line = line.strip()
            
            if line.startswith('Timestamp:'):
                timestamp = line.split('Timestamp:')[1].strip()
            elif line.startswith('[ ID]'):
                continue
            elif line.startswith('[') and timestamp is not None:
                parts = line.split()
                if parts[-1] == 'sender' and len(parts) > 6:
                    bitrate_str = parts[6]
                    if 'Mbits/sec' in parts:
                        bitrate = float(bitrate_str)
                    elif 'Kbits/sec' in parts:
                        bitrate = float(bitrate_str) / 1000
                    temp[timestamp] = bitrate
    sorted_temp = dict(sorted(temp.items()))
    timestamps = list(sorted_temp.keys())
    bitrates = list(sorted_temp.values())
    return timestamps, bitrates

output_notebook()

file_path = 'soal_chart_bokeh.txt'

timestamps, bitrates = parse_data(file_path)
print(timestamps, bitrates)

unique_timestamps = list(timestamps)

p = figure(title="Testing Jaringan", x_axis_label='DATE TIME', y_axis_label='Speed (Mbps)', x_range=timestamps, x_axis_type='auto')

p.line(timestamps, bitrates, line_width=2, color='blue')

p.xaxis.major_label_orientation = 1.2

output_file('testing_jaringan.html')

show(p)