import streamlit as st

# --- إعدادات الصفحة (الاسم والشعار الملكي للمتجر) ---
st.set_page_config(
    page_title="MORA STORE", 
    page_icon="👑", 
    layout="centered"
)

# --- إدارة حالة تسجيل الدخول، اسم المستخدم، وعربة التسوق ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# --- تصميم الألوان المبتكر والخلاب (CSS) ---
st.markdown("""
    <style>
        /* خلفية متدرجة فخمة بألوان عصرية مريحة للعين */
        .stApp {
            background: linear-gradient(135deg, #1f4068 0%, #162447 50%, #1b1b2f 100%);
            color: #ffffff;
        }
        
        /* تنسيق العناوين بألوان ناصعة وظلال مميزة */
        h1, h2, h3 {
            color: #e4e4e4;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
        }

        /* تنسيق الزراير بألوان جذابة مع تأثيرات انسيابية */
        div.stButton > button {
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            border-radius: 25px;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover {
            background: linear-gradient(45deg, #ff4b2b, #ff416c);
            box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
            transform: translateY(-2px);
        }
        
        /* تنسيق صناديق الإدخال */
        div.stTextInput > div > div > input {
            border-radius: 12px;
            border: 2px solid #00adb5;
            background-color: #0f172a;
            color: white;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- صفحة تسجيل الدخول ---
def show_login_page():
    # عرض صورة الشعار/اللوجو في أعلى صفحة تسجيل الدخول
    col_l1, col_l2, col_l3 = st.columns([1, 1, 1])
    with col_l2:
        try:
            st.image("logo.jpg", use_column_width=True)
        except:
            st.write("👑")
            
    st.markdown("<h1>MORA STORE</h1>", unsafe_allow_html=True)
    st.markdown("<h3>مرحباً بك، يرجى تسجيل الدخول للبدء</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("---")
        username = st.text_input("اسم المستخدم", placeholder="ادخل اسمك هنا...")
        password = st.text_input("كلمة المرور", type="password", placeholder="••••••••")
        
        login_button = st.button("تسجيل الدخول")
        
        if login_button:
            if username.strip() != "" and password == "12345":
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = username.strip()
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            elif username == "" or password == "":
                 st.warning("الرجاء إدخال اسم المستخدم وكلمة المرور.")
            else:
                st.error("كلمة المرور غير صحيحة، يرجى المحاولة مرة أخرى.")

    # حقوق الطبع والنشر في الأسفل
    st.write("\n\n")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>© 2026 MORA STORE. All Rights Reserved.</p>", unsafe_allow_html=True)

# --- صفحة المنتجات والترحيب بالاسم ---
def show_products_page():
    user = st.session_state['user_name']
    
    # رأس الصفحة (عرض اللوجو + الترحيب بالاسم + زر الفاتورة)
    col_top1, col_top2 = st.columns([3, 1])
    with col_top1:
        st.markdown(f"<h2>Hello, {user}! 👋</h2>", unsafe_allow_html=True)
    with col_top2:
        cart_count = len(st.session_state['cart'])
        if st.button(f"🛒 الفاتورة ({cart_count})"):
            st.session_state['show_cart'] = True
            st.rerun()

    # عرض اللوجو تحت الترحيب مباشرة
    col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
    with col_img2:
        try:
            st.image("logo.jpg", width=120)
        except:
            pass

    st.markdown("<p style='text-align: center; color: #00adb5; font-size: 18px;'>استمتع بأحدث تشكيلة من منتجات وعطور وأكسسوارات MORA CLOTHING الفخمة</p>", unsafe_allow_html=True)
    st.write("---")
    
    # تعريف جميع المنتجات بما فيها العطرين (perfume.jpg و perfume2.jpg)
    products = [
        {"name": "هودي MORA الأسود", "price": 450, "img": "tshirt.jpg", "key": "tshirt_btn"},
        {"name": "شروال MORA الرياضي", "price": 350, "img": "pants.jpg", "key": "pants_btn"},
        {"name": "الطقم الكامل MORA", "price": 750, "img": "full_suit.jpg", "key": "suit_btn"},
        {"name": "عطر MORA كلاسيك", "price": 500, "img": "perfume.jpg", "key": "perfume_btn"},
        {"name": "عطر MORA الملكي", "price": 600, "img": "perfume2.jpg", "key": "perfume2_btn"},
        {"name": "ساعة MORA الفاخرة", "price": 850, "img": "watch.jpg", "key": "watch_btn"},
        {"name": "الحذاء الرياضي العصري", "price": 550, "img": "sneakers.jpg", "key": "sneakers_btn"},
        {"name": "الجاكيت الجلد العصري", "price": 950, "img": "jacket.jpg", "key": "jacket_btn"},
        {"name": "النظارة الشمسية MORA", "price": 400, "img": "sunglasses.jpg", "key": "sunglasses_btn"},
        {"name": "السوار المعدني الفاخر", "price": 250, "img": "bracelet.jpg", "key": "bracelet_btn"}
    ]

    # عرض المنتجات في شبكة (كل صف منتجين)
    for i in range(0, len(products), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            p1 = products[i]
            st.subheader(p1["name"])
            st.image(p1["img"], use_column_width=True)
            st.markdown(f"**السعر:** {p1['price']} جنيه")
            if st.button("إضافة للعربة", key=p1["key"]):
                st.session_state['cart'].append({"name": p1["name"], "price": p1["price"]})
                st.success(f"تمت إضافة {p1['name']} إلى الفاتورة بنجاح!")

        if i + 1 < len(products):
            with col2:
                p2 = products[i + 1]
                st.subheader(p2["name"])
                st.image(p2["img"], use_column_width=True)
                st.markdown(f"**السعر:** {p2['price']} جنيه")
                if st.button("إضافة للعربة", key=p2["key"]):
                    st.session_state['cart'].append({"name": p2["name"], "price": p2["price"]})
                    st.success(f"تمت إضافة {p2['name']} إلى الفاتورة بنجاح!")
        
        st.write("---")

    # زر تسجيل الخروج وحقوق النشر في الأسفل
    st.write("\n")
    col_bt1, col_bt2, col_bt3 = st.columns([1, 2, 1])
    with col_bt2:
        if st.button("🚪 تسجيل الخروج"):
            st.session_state['logged_in'] = False
            st.session_state['user_name'] = ""
            st.session_state['cart'] = []
            st.session_state['show_cart'] = False
            st.rerun()

    st.write("---")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>© 2026 MORA STORE. All Rights Reserved.</p>", unsafe_allow_html=True)

# --- صفحة الفاتورة وعربة التسوق ---
def show_cart_page():
    user = st.session_state['user_name']
    st.markdown(f"<h1>🧾 فاتورة المشتريات الخاصة بـ {user}</h1>", unsafe_allow_html=True)
    st.write("---")
    
    if len(st.session_state['cart']) == 0:
        st.info("عربة التسوق فارغة حالياً. لم تقم بإضافة أي منتجات بعد.")
    else:
        total_price = 0
        for idx, item in enumerate(st.session_state['cart'], 1):
            st.markdown(f"**{idx}. {item['name']}** — `{item['price']} جنيه`")
            total_price += item['price']
        
        st.write("---")
        st.markdown(f"<h3>الإجمالي الكلي: {total_price} جنيه</h3>", unsafe_allow_html=True)
        
        # زر طباعة الفاتورة
        if st.button("🖨️ طباعة الفاتورة"):
            st.components.v1.html("<script>window.print();</script>", height=0)
            st.info("جاري فتح نافذة الطباعة...")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("إتمام الشراء"):
                st.success("🎉 تم تأكيد طلبك بنجاح! شكراً لتسوقك في MORA STORE.")
                st.session_state['cart'] = []
        with col_btn2:
            if st.button("تفريغ الفاتورة"):
                st.session_state['cart'] = []
                st.rerun()

    st.write("---")
    if st.button("العودة إلى المتجر"):
        st.session_state['show_cart'] = False
        st.rerun()

    # زر تسجيل الخروج وحقوق النشر في الأسفل
    st.write("\n")
    col_bt1, col_bt2, col_bt3 = st.columns([1, 2, 1])
    with col_bt2:
        if st.button("🚪 تسجيل الخروج", key="logout_cart"):
            st.session_state['logged_in'] = False
            st.session_state['user_name'] = ""
            st.session_state['cart'] = []
            st.session_state['show_cart'] = False
            st.rerun()

    st.write("---")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>© 2026 MORA STORE. All Rights Reserved.</p>", unsafe_allow_html=True)

# --- التحكم في التنقل بين الصفحات ---
if not st.session_state['logged_in']:
    show_login_page()
else:
    if 'show_cart' not in st.session_state:
        st.session_state['show_cart'] = False
    
    if st.session_state['show_cart']:
        show_cart_page()
    else:
        show_products_page()