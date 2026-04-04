#!/usr/bin/python3
"""Module to find and replace a string in the heap of a running process."""

import sys


def read_write_heap(pid, search_string, replace_string):
    """Find and replace a string in the heap of a running process.

    Args:
        pid (str): The process ID of the running process.
        search_string (str): The ASCII string to search for in the heap.
        replace_string (str): The ASCII string to replace the found string with.
    """
    maps_file = "/proc/{}/maps".format(pid)
    mem_file = "/proc/{}/mem".format(pid)

    try:
        with open(maps_file, 'r') as maps:
            heap_start = None
            heap_end = None

            for line in maps:
                if '[heap]' in line:
                    addr_range = line.split()[0]
                    heap_start, heap_end = addr_range.split('-')
                    heap_start = int(heap_start, 16)
                    heap_end = int(heap_end, 16)
                    break

        if heap_start is None:
            print("Could not find heap in process maps")
            sys.exit(1)

        print("Heap found: 0x{:x} - 0x{:x}".format(heap_start, heap_end))

        with open(mem_file, 'rb+') as mem:
            mem.seek(heap_start)
            heap_data = mem.read(heap_end - heap_start)

            search_bytes = search_string.encode('ASCII')
            replace_bytes = replace_string.encode('ASCII')

            offset = heap_data.find(search_bytes)
            if offset == -1:
                print("String '{}' not found in heap".format(search_string))
                sys.exit(1)

            print("String '{}' found at offset: 0x{:x}".format(
                search_string, offset))
            print("Replacing with '{}'...".format(replace_string))

            mem.seek(heap_start + offset)
            mem.write(replace_bytes)

            print("Done!")

    except PermissionError:
        print("Permission denied. Try running with sudo.")
        sys.exit(1)
    except FileNotFoundError:
        print("Process {} not found.".format(pid))
        sys.exit(1)


def main():
    """Validate arguments and call read_write_heap."""
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if not pid.isdigit():
        print("Error: pid must be a number")
        sys.exit(1)

    read_write_heap(pid, search_string, replace_string)


if __name__ == "__main__":
    main()
