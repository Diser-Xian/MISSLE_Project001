# 🔴 EXTREME LONG ERROR SIMULATOR 🔴
import time
import random

RED = "\033[91m"
RESET = "\033[0m"

errors = [
    "Segmentation fault (core dumped)",
    "Stack overflow detected in main thread",
    "Memory leak at address 0x0000FFAA",
    "NullPointerException: object reference not set",
    "Kernel panic - not syncing",
    "Fatal runtime error: invalid opcode",
    "Buffer overflow in process handler",
    "Access violation at memory location 0xFFFFFFFF",
    "Thread deadlock detected",
    "System call failed: permission denied",
]

def long_error_block(i):
    print(RED + "="*60)
    print(f"[CRITICAL ERROR #{i}] SYSTEM FAILURE DETECTED")
    print("-"*60)

    for _ in range(8):  # spam multiple lines
        err = random.choice(errors)
        hex_addr = hex(random.randint(0, 999999999))
        print(f"> {err} | Address: {hex_addr}")

    print("-"*60)
    print("Dumping stack trace...\n")

    # fake stack trace
    for j in range(5):
        print(f"  File \"system_module_{j}.py\", line {random.randint(10,200)}, in execute")
        print(f"    process_data(chunk_{j})")

    print("="*60 + RESET)


counter = 1

while True:
    try:
        long_error_block(counter)
        time.sleep(0.4)

        # trigger a REAL error occasionally
        if counter % 3 == 0:
            crash = 10 / 0  # real crash

        counter += 1

    except Exception as e:
        print(RED + "\n[!!! EXCEPTION CAUGHT !!!]")
        print(f"> {e}")
        print("[SYSTEM] Attempting unstable recovery...")
        print("[WARNING] Data corruption possible...\n" + RESET)
        time.sleep(1)

        # keep looping forever 😈
        counter += 1