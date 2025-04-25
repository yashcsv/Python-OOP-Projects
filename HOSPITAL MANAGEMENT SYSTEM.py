import os
import sqlite3
import getpass
import time



class system_menu:
    def __init__(self):
        self.setup_database()
        self.first_page()
        
    def setup_database(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''     
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                dob TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


    def invalid_input_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                             ⚠ ERROR                               ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║                                                                    ║
        ║   Invalid input detected!                                          ║
        ║   Please enter only '1' to Login or '2' to Register.               ║
        ║                                                                    ║
        ║   Returning to main menu in 3 seconds...                           ║
        ║                                                                    ║
        ╚════════════════════════════════════════════════════════════════════╝
        ''')
        time.sleep(3)
        return self.first_page()


    def first_page(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        option_1 = input('''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                        HOSPITAL MANAGEMENT SYSTEM                  ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║                                                                    ║
        ║   Welcome to the Hospital Management System Terminal Interface.    ║
        ║   Please choose from the following options:                        ║
        ║                                                                    ║
        ║       [1]  Login to your existing account                          ║
        ║       [2]  Register as a new user                                  ║
        ║                                                                    ║
        ║   To proceed, enter the corresponding number (1 or 2):             ║
        ║                                                                    ║
        ╚════════════════════════════════════════════════════════════════════╝
        ''')
        if option_1 == '1':
            return self.login_page()
        elif option_1 == '2':
            return self.register_page()
        else:
            return self.invalid_input_screen()

    def login_page(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                              LOGIN                                 ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║ Please enter your username and password to log in:                 ║
        ╚════════════════════════════════════════════════════════════════════╝
        ''')
        username = input("  Username : ")
        password = getpass.getpass("  Password : ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                      LOGIN SUCCESSFUL                              ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║ Welcome back, {user[1]}!                                           ║
        ║ You are now logged in.                                             ║
        ╚════════════════════════════════════════════════════════════════════╝
            ''')
            time.sleep(3)
            return HomePage(user[7])  # Pass username to HomePage
        else:
            print("\n❌ Invalid username or password. Please try again.")
            time.sleep(3)
            return self.first_page()

    def register_page(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                         USER REGISTRATION                          ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║ Please fill out the following information to register:             ║
        ╚════════════════════════════════════════════════════════════════════╝
        ''')
        name = input("  Full Name                 : ")
        age = input("  Age                       : ")
        gender = input("  Gender (M/F/Other)        : ")
        dob = input("  Date of Birth (YYYY-MM-DD): ")
        email = input("  Email Address             : ")
        phone = input("  Phone Number              : ")
        username = input("  Desired Username          : ")
        password = getpass.getpass("  Create a Password         : ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()

        cursor.execute('''     
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                dob TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        try:
            cursor.execute('''
                INSERT INTO users (name, age, gender, dob, email, phone, username, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, int(age), gender, dob, email, phone, username, password))
            conn.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                        REGISTRATION SUCCESSFUL!                    ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║ You have been successfully registered.                             ║
        ║ You can now log in using your credentials.                         ║
        ╚════════════════════════════════════════════════════════════════════╝
            ''')
            time.sleep(3)
        except sqlite3.IntegrityError as e:
            print("\n❌ Error: Email, phone number, or username already exists!")
            print("Details:", e)
            time.sleep(3)
        finally:
            conn.close()
            return self.first_page()






class HomePage:
    def __init__(self, username):
        self.username = username
        self.show_home_page()

    def show_home_page(self):
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
        ╔════════════════════════════════════════════════════════════════════╗
        ║                  HOSPITAL MANAGEMENT SYSTEM - HOME                 ║
        ╠════════════════════════════════════════════════════════════════════╣
        ║ Welcome, {self.username}!                                          
        ║                                                                   
        ║ What is a Hospital Management System (HMS)?                        ║
        ║ It is a digital platform used by hospitals, clinics,               ║
        ║ and healthcare institutions to manage critical operations:        
        ║                                                                   
        ║   [1] ✅ Patient Records Management                                 
        ║   [2] 📅 Appointment Scheduling                                    
        ║   [3] 💰 Billing & Payments                                        
        ║   [4] 🧑‍⚕️ Doctor/Nurse Scheduling                                 
        ║   [5] 💊 Pharmacy Inventory                                        
        ║   [6] 🧪 Lab & Diagnostic Management                                
        ║   [7] 📝 Insurance Processing                                      
        ║   [8] 📊 Admin Reports                                             
        ║   [9] 🔒 Logout                                                    
        ║                                                                   
        ╚════════════════════════════════════════════════════════════════════╝
        ''')
                    choice = input("Select an option (1-9): ")
        
                    if choice == '1':
                        return PatientRecords(self.username)
                    elif choice == '2':
                        return AppointmentScheduler(self.username)
                    elif choice == '3':
                        return BillingSystem(self.username)
                    elif choice == '4':
                        return StaffScheduler(self.username)
                    elif choice == '5':
                        return PharmacyInventory(self.username)
                    elif choice == '6':
                        return LabDiagnostics(self.username)
                    elif choice == '7':
                        return InsuranceProcessing(self.username)
                    elif choice == '8':
                        return AdminReports(self.username)
                    elif choice == '9':
                        print("Logging out...")
                        time.sleep(2)
                        return system_menu().first_page()
                    else:
                        print("🚧 Module not yet implemented.")
                        time.sleep(2)








class PatientRecords(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                dob TEXT,
                phone TEXT,
                address TEXT,
                medical_history TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════════╗
║                    PATIENT RECORDS MANAGEMENT                      ║
╠════════════════════════════════════════════════════════════════════╣
║  [1] Add New Patient Record                                        ║
║  [2] View All Patient Records                                      ║
║  [3] Update Existing Patient                                       ║
║  [4] Delete Patient Record                                         ║
║  [5] Return to Home Page                                           ║
╚════════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.view_patients()
            elif choice == '3':
                self.update_patient()
            elif choice == '4':
                self.delete_patient()
            elif choice == '5':
                return HomePage(self.username)
            else:
                print("Invalid choice!")
                time.sleep(2)

    def add_patient(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📝 Add New Patient Record\n")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        phone = input("Phone: ")
        address = input("Address: ")
        medical_history = input("Medical History: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (name, age, gender, dob, phone, address, medical_history)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, gender, dob, phone, address, medical_history))
        conn.commit()
        conn.close()

        print("\n✅ Patient added successfully!")
        input("Press Enter to continue...")

    def view_patients(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📋 All Patient Records:\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients')
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, DOB: {row[4]}, Phone: {row[5]}")
                print(f"Address: {row[6]}")
                print(f"Medical History: {row[7]}")
                print("-" * 60)
        else:
            print("No records found.")
        
        input("\nPress Enter to return...")

    def update_patient(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("✏️ Update Patient Record\n")
        pid = input("Enter Patient ID to update: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id = ?', (pid,))
        patient = cursor.fetchone()

        if not patient:
            print("❌ Patient not found.")
            conn.close()
            time.sleep(2)
            return

        name = input(f"Name [{patient[1]}]: ") or patient[1]
        age = input(f"Age [{patient[2]}]: ") or patient[2]
        gender = input(f"Gender [{patient[3]}]: ") or patient[3]
        dob = input(f"DOB [{patient[4]}]: ") or patient[4]
        phone = input(f"Phone [{patient[5]}]: ") or patient[5]
        address = input(f"Address [{patient[6]}]: ") or patient[6]
        medical_history = input(f"Medical History [{patient[7]}]: ") or patient[7]

        cursor.execute('''
            UPDATE patients
            SET name = ?, age = ?, gender = ?, dob = ?, phone = ?, address = ?, medical_history = ?
            WHERE id = ?
        ''', (name, age, gender, dob, phone, address, medical_history, pid))
        conn.commit()
        conn.close()

        print("\n✅ Patient record updated.")
        input("Press Enter to continue...")

    def delete_patient(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑 Delete Patient Record\n")
        pid = input("Enter Patient ID to delete: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM patients WHERE id = ?', (pid,))
        conn.commit()
        conn.close()

        print("✅ Patient record deleted.")
        input("Press Enter to continue...")







class AppointmentScheduler(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                doctor_name TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                reason TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════════╗
║                     APPOINTMENT SCHEDULING MENU                    ║
╠════════════════════════════════════════════════════════════════════╣
║  [1] Schedule New Appointment                                      ║
║  [2] View All Appointments                                         ║
║  [3] Cancel Appointment                                            ║
║  [4] Return to Home Page                                           ║
╚════════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.schedule_appointment()
            elif choice == '2':
                self.view_appointments()
            elif choice == '3':
                self.cancel_appointment()
            elif choice == '4':
                return HomePage(self.username)
            else:
                print("Invalid choice!")
                time.sleep(2)

    def schedule_appointment(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📅 Schedule New Appointment\n")
        patient_name = input("Patient Name     : ")
        doctor_name = input("Doctor Name      : ")
        date = input("Appointment Date (YYYY-MM-DD): ")
        time_slot = input("Appointment Time (HH:MM): ")
        reason = input("Reason (optional): ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (patient_name, doctor_name, date, time, reason)
            VALUES (?, ?, ?, ?, ?)
        ''', (patient_name, doctor_name, date, time_slot, reason))
        conn.commit()
        conn.close()

        print("\n✅ Appointment scheduled successfully!")
        input("Press Enter to continue...")

    def view_appointments(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📋 All Appointments:\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        conn.close()

        if appointments:
            for app in appointments:
                print(f"ID: {app[0]} | Patient: {app[1]} | Doctor: {app[2]} | Date: {app[3]} | Time: {app[4]} | Reason: {app[5]}")
                print("-" * 60)
        else:
            print("No appointments found.")
        
        input("\nPress Enter to return...")

    def cancel_appointment(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑 Cancel Appointment\n")
        app_id = input("Enter Appointment ID to cancel: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM appointments WHERE id = ?', (app_id,))
        conn.commit()
        conn.close()

        print("✅ Appointment cancelled.")
        input("Press Enter to continue...")




class BillingSystem(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                services TEXT NOT NULL,
                total_amount REAL NOT NULL,
                paid INTEGER DEFAULT 0,
                payment_mode TEXT,
                date TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════════╗
║                        BILLING & PAYMENTS MENU                     ║
╠════════════════════════════════════════════════════════════════════╣
║  [1] Generate New Bill                                             ║
║  [2] View All Bills                                                ║
║  [3] Mark Bill as Paid                                             ║
║  [4] Return to Home Page                                           ║
╚════════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.generate_bill()
            elif choice == '2':
                self.view_bills()
            elif choice == '3':
                self.mark_paid()
            elif choice == '4':
                return HomePage(self.username)
            else:
                print("Invalid choice!")
                time.sleep(2)

    def generate_bill(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🧾 Generate New Bill\n")
        patient_name = input("Patient Name       : ")
        services = input("Services Provided  : ")
        total_amount = float(input("Total Amount (₹)   : "))
        date = input("Billing Date (YYYY-MM-DD): ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bills (patient_name, services, total_amount, date)
            VALUES (?, ?, ?, ?)
        ''', (patient_name, services, total_amount, date))
        conn.commit()
        conn.close()

        print("\n✅ Bill generated successfully!")
        input("Press Enter to continue...")

    def view_bills(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📄 All Bills:\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bills')
        bills = cursor.fetchall()
        conn.close()

        if bills:
            for bill in bills:
                status = "PAID" if bill[4] else "UNPAID"
                print(f"ID: {bill[0]} | Patient: {bill[1]} | Amount: ₹{bill[3]:.2f} | Status: {status} | Date: {bill[6]} | Mode: {bill[5] or 'N/A'}")
                print(f"Services: {bill[2]}")
                print("-" * 60)
        else:
            print("No bills found.")
        
        input("\nPress Enter to return...")

    def mark_paid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("💵 Mark Bill as Paid\n")
        bill_id = input("Enter Bill ID to mark as paid: ")
        mode = input("Payment Mode (Cash/Card/UPI/NetBanking): ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE bills SET paid = 1, payment_mode = ?
            WHERE id = ?
        ''', (mode, bill_id))
        conn.commit()
        conn.close()

        print("✅ Payment updated successfully.")
        input("Press Enter to continue...")



class StaffScheduler(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff_schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_name TEXT NOT NULL,
                role TEXT CHECK(role IN ('Doctor', 'Nurse')) NOT NULL,
                department TEXT NOT NULL,
                shift TEXT CHECK(shift IN ('Morning', 'Afternoon', 'Night')) NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔══════════════════════════════════════════════════════════════════╗
║                DOCTOR / NURSE SCHEDULING MENU                    ║
╠══════════════════════════════════════════════════════════════════╣
║  [1] Add Staff Schedule                                          ║
║  [2] View Schedules                                              ║
║  [3] Delete Schedule                                             ║
║  [4] Return to Home Page                                         ║
╚══════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_schedule()
            elif choice == '2':
                self.view_schedules()
            elif choice == '3':
                self.delete_schedule()
            elif choice == '4':
                return HomePage(self.username)
            else:
                print("❌ Invalid choice!")
                time.sleep(2)

    def add_schedule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📋 Add Staff Schedule\n")
        staff_name = input("Staff Name      : ")
        role = input("Role (Doctor/Nurse) : ").capitalize()
        department = input("Department       : ")
        shift = input("Shift (Morning/Afternoon/Night) : ").capitalize()
        date = input("Date (YYYY-MM-DD): ")

        if role not in ['Doctor', 'Nurse'] or shift not in ['Morning', 'Afternoon', 'Night']:
            print("❌ Invalid role or shift. Please try again.")
            time.sleep(2)
            return

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO staff_schedule (staff_name, role, department, shift, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (staff_name, role, department, shift, date))
        conn.commit()
        conn.close()

        print("\n✅ Schedule added successfully!")
        input("Press Enter to continue...")

    def view_schedules(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📅 All Schedules:\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM staff_schedule ORDER BY date')
        schedules = cursor.fetchall()
        conn.close()

        if schedules:
            for s in schedules:
                print(f"ID: {s[0]} | Name: {s[1]} | Role: {s[2]} | Dept: {s[3]} | Shift: {s[4]} | Date: {s[5]}")
                print("-" * 60)
        else:
            print("No schedules found.")
        input("\nPress Enter to return...")

    def delete_schedule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑️ Delete Schedule\n")
        schedule_id = input("Enter Schedule ID to delete: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM staff_schedule WHERE id = ?', (schedule_id,))
        conn.commit()
        conn.close()

        print("✅ Schedule deleted successfully.")
        input("Press Enter to continue...")




class PharmacyInventory(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pharmacy_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_name TEXT NOT NULL,
                manufacturer TEXT,
                quantity INTEGER NOT NULL,
                price_per_unit REAL NOT NULL,
                expiry_date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════╗
║                PHARMACY INVENTORY MANAGEMENT                   ║
╠════════════════════════════════════════════════════════════════╣
║  [1] Add Medicine                                              ║
║  [2] View Inventory                                            ║
║  [3] Update Medicine Stock                                     ║
║  [4] Delete Medicine                                           ║
║  [5] Check Low Stock                                           ║
║  [6] Return to Home Page                                       ║
╚════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_medicine()
            elif choice == '2':
                self.view_inventory()
            elif choice == '3':
                self.update_stock()
            elif choice == '4':
                self.delete_medicine()
            elif choice == '5':
                self.check_low_stock()
            elif choice == '6':
                return HomePage(self.username)
            else:
                print("❌ Invalid choice!")
                time.sleep(2)

    def add_medicine(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("➕ Add New Medicine\n")
        name = input("Medicine Name      : ")
        manufacturer = input("Manufacturer        : ")
        quantity = int(input("Quantity            : "))
        price = float(input("Price per Unit (₹)  : "))
        expiry = input("Expiry Date (YYYY-MM-DD): ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pharmacy_inventory (medicine_name, manufacturer, quantity, price_per_unit, expiry_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, manufacturer, quantity, price, expiry))
        conn.commit()
        conn.close()

        print("✅ Medicine added successfully.")
        input("Press Enter to continue...")

    def view_inventory(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📦 Pharmacy Inventory:\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pharmacy_inventory ORDER BY expiry_date')
        meds = cursor.fetchall()
        conn.close()

        if meds:
            for m in meds:
                print(f"ID: {m[0]} | Name: {m[1]} | Qty: {m[3]} | ₹{m[4]:.2f} | Exp: {m[5]} | Manufacturer: {m[2]}")
                print("-" * 60)
        else:
            print("⚠️ No medicine records found.")
        input("\nPress Enter to return...")

    def update_stock(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🔄 Update Medicine Stock\n")
        med_id = input("Enter Medicine ID: ")
        new_qty = int(input("New Quantity      : "))

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE pharmacy_inventory SET quantity = ? WHERE id = ?', (new_qty, med_id))
        conn.commit()
        conn.close()

        print("✅ Stock updated successfully.")
        input("Press Enter to continue...")

    def delete_medicine(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑️ Delete Medicine\n")
        med_id = input("Enter Medicine ID to delete: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM pharmacy_inventory WHERE id = ?', (med_id,))
        conn.commit()
        conn.close()

        print("✅ Medicine deleted successfully.")
        input("Press Enter to continue...")

    def check_low_stock(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("⚠️ Low Stock Medicines (< 10 units):\n")
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pharmacy_inventory WHERE quantity < 10')
        meds = cursor.fetchall()
        conn.close()

        if meds:
            for m in meds:
                print(f"ID: {m[0]} | Name: {m[1]} | Qty: {m[3]} | Exp: {m[5]}")
                print("-" * 60)
        else:
            print("✅ All medicines are well-stocked.")
        input("\nPress Enter to return...")




class LabDiagnostics(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lab_tests (
                test_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                test_name TEXT NOT NULL,
                test_date TEXT NOT NULL,
                result TEXT DEFAULT 'Pending',
                doctor TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════╗
║                   LAB & DIAGNOSTIC MANAGEMENT                  ║
╠════════════════════════════════════════════════════════════════╣
║  [1] Add New Lab Test                                          ║
║  [2] View All Tests                                            ║
║  [3] Update Test Result                                        ║
║  [4] Delete Test Record                                        ║
║  [5] Return to Home Page                                       ║
╚════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_test()
            elif choice == '2':
                self.view_tests()
            elif choice == '3':
                self.update_result()
            elif choice == '4':
                self.delete_test()
            elif choice == '5':
                return HomePage(self.username)
            else:
                print("❌ Invalid input.")
                time.sleep(2)

    def add_test(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🧪 Add New Lab Test\n")
        name = input("Patient Name       : ")
        test = input("Test Name          : ")
        date = input("Test Date (YYYY-MM-DD): ")
        doctor = input("Referred by Doctor : ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lab_tests (patient_name, test_name, test_date, doctor)
            VALUES (?, ?, ?, ?)
        ''', (name, test, date, doctor))
        conn.commit()
        conn.close()

        print("✅ Lab test added successfully.")
        input("Press Enter to continue...")

    def view_tests(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📋 All Lab Test Records:\n")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM lab_tests ORDER BY test_date DESC')
        tests = cursor.fetchall()
        conn.close()

        if tests:
            for t in tests:
                print(f"ID: {t[0]} | Patient: {t[1]} | Test: {t[2]} | Date: {t[3]} | Result: {t[4]} | Doctor: {t[5]}")
                print("-" * 70)
        else:
            print("⚠️ No test records found.")
        input("\nPress Enter to return...")

    def update_result(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📝 Update Lab Test Result\n")
        test_id = input("Enter Test ID: ")
        result = input("Enter Test Result: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE lab_tests SET result = ? WHERE test_id = ?', (result, test_id))
        conn.commit()
        conn.close()

        print("✅ Result updated.")
        input("Press Enter to continue...")

    def delete_test(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑️ Delete Lab Test Record\n")
        test_id = input("Enter Test ID to delete: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM lab_tests WHERE test_id = ?', (test_id,))
        conn.commit()
        conn.close()

        print("✅ Test record deleted.")
        input("Press Enter to continue...")





class InsuranceProcessing(HomePage):
    def __init__(self, username):
        self.username = username
        self.db_setup()
        self.menu()

    def db_setup(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS insurance_claims (
                claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                insurance_provider TEXT NOT NULL,
                policy_number TEXT NOT NULL,
                claim_amount REAL NOT NULL,
                status TEXT DEFAULT 'Pending',
                claim_date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════╗
║                   INSURANCE PROCESSING CENTER                  ║
╠════════════════════════════════════════════════════════════════╣
║  [1] File Insurance Claim                                      ║
║  [2] View All Claims                                           ║
║  [3] Approve/Reject Claim                                      ║
║  [4] Delete Claim Record                                       ║
║  [5] Return to Home Page                                       ║
╚════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_claim()
            elif choice == '2':
                self.view_claims()
            elif choice == '3':
                self.update_claim_status()
            elif choice == '4':
                self.delete_claim()
            elif choice == '5':
                return HomePage(self.username)
            else:
                print("❌ Invalid input.")
                time.sleep(2)

    def add_claim(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📝 File New Insurance Claim\n")
        name = input("Patient Name        : ")
        provider = input("Insurance Provider  : ")
        policy = input("Policy Number       : ")
        amount = float(input("Claim Amount (₹)    : "))
        date = input("Claim Date (YYYY-MM-DD): ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO insurance_claims (patient_name, insurance_provider, policy_number, claim_amount, claim_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, provider, policy, amount, date))
        conn.commit()
        conn.close()

        print("✅ Insurance claim filed successfully.")
        input("Press Enter to continue...")

    def view_claims(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📋 All Insurance Claims:\n")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM insurance_claims ORDER BY claim_date DESC')
        claims = cursor.fetchall()
        conn.close()

        if claims:
            for c in claims:
                print(f"ID: {c[0]} | Patient: {c[1]} | Provider: {c[2]} | Policy: {c[3]} | Amount: ₹{c[4]:.2f} | Status: {c[5]} | Date: {c[6]}")
                print("-" * 70)
        else:
            print("⚠️ No insurance claims found.")
        input("\nPress Enter to return...")

    def update_claim_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🔁 Update Claim Status\n")
        claim_id = input("Enter Claim ID: ")
        new_status = input("Enter New Status (Approved/Rejected): ").capitalize()

        if new_status not in ["Approved", "Rejected"]:
            print("❌ Invalid status. Must be 'Approved' or 'Rejected'.")
            time.sleep(2)
            return

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE insurance_claims SET status = ? WHERE claim_id = ?', (new_status, claim_id))
        conn.commit()
        conn.close()

        print("✅ Claim status updated.")
        input("Press Enter to continue...")

    def delete_claim(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🗑️ Delete Insurance Claim\n")
        claim_id = input("Enter Claim ID to delete: ")

        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM insurance_claims WHERE claim_id = ?', (claim_id,))
        conn.commit()
        conn.close()

        print("✅ Claim record deleted.")
        input("Press Enter to continue...")




class AdminReports(HomePage):
    def __init__(self, username):
        self.username = username
        self.menu()

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
╔════════════════════════════════════════════════════════════════╗
║                        ADMIN REPORTS CENTER                    ║
╠════════════════════════════════════════════════════════════════╣
║  [1] Patient & Appointment Summary                             ║
║  [2] Financial Summary (Revenue Report)                        ║
║  [3] Staff Scheduling Summary                                  ║
║  [4] Insurance Claims Summary                                  ║
║  [5] Return to Home Page                                       ║
╚════════════════════════════════════════════════════════════════╝
''')
            choice = input("Enter your choice: ")

            if choice == '1':
                self.patient_summary()
            elif choice == '2':
                self.financial_summary()
            elif choice == '3':
                self.staff_summary()
            elif choice == '4':
                self.insurance_summary()
            elif choice == '5':
                return HomePage(self.username)
            else:
                print("❌ Invalid option.")
                time.sleep(2)

    def patient_summary(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM patients")
        total_patients = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM appointments")
        total_appointments = cursor.fetchone()[0]

        conn.close()

        print(f"\n👤 Total Patients      : {total_patients}")
        print(f"📅 Total Appointments : {total_appointments}")
        input("\nPress Enter to return...")


    def financial_summary(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
    
        cursor.execute("SELECT SUM(total_amount) FROM bills WHERE paid = 1")
        total_revenue = cursor.fetchone()[0] or 0.0
    
        conn.close()
    
        print(f"\n💰 Total Revenue Collected: ₹{total_revenue:.2f}")
        input("\nPress Enter to return...")

    def staff_summary(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM staff_schedule")
        total_shifts = cursor.fetchone()[0]

        cursor.execute("SELECT DISTINCT role FROM staff_schedule")
        roles = [r[0] for r in cursor.fetchall()]

        print(f"\n🧑‍⚕️ Total Staff Shifts Scheduled: {total_shifts}")
        print("📌 Staff Roles Scheduled:")
        for role in roles:
            print(f"   - {role}")
        conn.close()
        input("\nPress Enter to return...")

    def insurance_summary(self):
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM insurance_claims")
        total_claims = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM insurance_claims WHERE status = 'Approved'")
        approved = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM insurance_claims WHERE status = 'Rejected'")
        rejected = cursor.fetchone()[0]

        pending = total_claims - (approved + rejected)

        print(f"\n📝 Total Claims Filed    : {total_claims}")
        print(f"✅ Approved Claims        : {approved}")
        print(f"❌ Rejected Claims        : {rejected}")
        print(f"⏳ Pending Claims         : {pending}")

        conn.close()
        input("\nPress Enter to return...")




obj = system_menu()
