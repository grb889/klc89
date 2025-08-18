# 🔧 Resize Your Kali Linux Virtual Machine Disk

This guide will walk you through the process of resizing your Kali Linux VM disk on a Windows host. This is useful if your virtual machine is running out of disk space and you need to expand it without reinstalling.

You'll learn how to:

1. Increase the size of the virtual hard disk using the `VBoxManage` command.
2. Expand the disk partition inside Kali using GParted.

---

## 🧱 PART 1: Resize the Virtual Disk Using `VBoxManage`

The `VBoxManage` tool allows you to modify VirtualBox VMs from the command line. We'll use it to resize your `.vdi` file (virtual disk image).

### ✅ Step 1: Shut Down the VM

Make sure your Kali VM is **completely powered off** — not suspended or in a saved state.

---

### ✅ Step 2: Open Command Prompt as Administrator

- Press `Win + S` and type `cmd`
- Right-click **Command Prompt** → choose **Run as administrator**

---

### ✅ Step 3: Navigate to the VirtualBox Directory

If VirtualBox is not already in your system `PATH`, run this:

```cmd
cd "C:\Program Files\Oracle\VirtualBox"
```

---

### ✅ Step 4: Resize the `.vdi` Virtual Disk File

Use the following command, **replacing the path** and size with your own values:

```cmd
VBoxManage modifyhd "C:\Users\YourName\VirtualBox VMs\Kali\Kali.vdi" --resize 30000
```

- `"..."` = Path to your `.vdi` file
- `30000` = New size in MB (e.g., 30 GB)

> 💡 **How to find the `.vdi` path:**
> - Open VirtualBox
> - Right-click your Kali VM → **Settings** → **Storage**
> - Click your disk under "Controller: SATA"
> - Look at the bottom for the full file path

If successful, you'll see the message:

```
0%...10%...20%...100%
Image resized successfully.
```

---

## 🧱 PART 2: Resize the Linux Partition Inside Kali

After expanding the virtual disk, you must resize the Linux partition inside the OS to actually use the new space.

---

### ✅ Step 5: Start Your Kali VM

Boot into Kali as usual.

---

### ✅ Step 6: Install GParted (Partition Editor)

Open a terminal and run:

```bash
sudo apt update
sudo apt install gparted
```

---

### ✅ Step 7: Launch GParted

In the terminal, type:

```bash
sudo gparted
```

This opens the graphical partition editor.

---

### ✅ Step 8: Resize the Main Partition

1. In GParted, locate your main partition (usually `/dev/sda1`)
2. Right-click the partition → select **Resize/Move**
3. Drag the slider to **use all unallocated space**
4. Click **Resize**
5. Then click the **green checkmark (✓)** to apply changes
6. Wait for the operation to finish
7. Close GParted and **reboot** the VM

---

### ✅ Step 9: Confirm the New Disk Size

After reboot, open a terminal and run:

```bash
df -h
```

You should now see increased space under `/dev/sda1` — for example:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        30G   5G   25G  17% /
```

---

## 🧠 Additional Tips

- Always **back up your VM** before resizing to avoid accidental data loss.
- If you're using **Snapshots**, delete or merge them before resizing, as `VBoxManage modifyhd` won’t work on a snapshot chain.
- If you prefer a GUI alternative, you can clone the VDI and specify a larger size during the clone process.

---

## ✅ Summary

| Task                                | Tool Used       | Notes                                 |
|-------------------------------------|------------------|----------------------------------------|
| Resize virtual disk                 | VBoxManage       | Command line on Windows                |
| Install partitioning tool           | GParted          | Installed via `apt` inside Kali        |
| Resize Linux file system partition  | GParted GUI      | Drag slider to expand space            |
| Confirm new space                   | `df -h` command  | Should show increased size on `/dev/sda1` |

---

With this guide, you can now confidently expand your Kali Linux VM's disk size — a crucial skill when working with large datasets in OSINT investigations.