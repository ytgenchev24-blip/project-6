import streamlit as st

st.title("My mini library app")

# Поправка: Проверяваме само st.session_state
if "books" not in st.session_state:
    st.session_state.books = []

st.header("Add book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)

if st.button("Add Book"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    # Поправка: Тези редове трябва да са навътре (1 Tab), за да са част от бутона
    st.session_state.books.append(book)
    st.success("The book is added!")

if st.button("View all books"):
    if len(st.session_state.books) == 0:
        st.write("No books")
    else:
        # Поправка: Трябва цикъл 'for', за да дефинираме променливата 'book'
        for book in st.session_state.books:
            st.write("Title:", book["title"])
            st.write("Author:", book["author"])
            st.write("Price:", book["price"])
            st.write("--------------------")

st.header("Search by author")
search_author = st.text_input("Enter author name")
if st.button("Search by author"):
    found = False
    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True # Поправка: Трябва да е навътре в 'if'

    if found == False: # Поправка: Трябва да е подравнено с 'for'
        st.write("There are no books by this author")

st.header("Search by title")
search_title = st.text_input("Enter title")
if st.button("Search by title"):
    found = False
    for book in st.session_state.books:
        if book["title"] == search_title:
            st.write(book)
            found = True

    if found == False: # Поправка: Трябва да е подравнено с 'for'
        st.write("No found book")

if st.button("Show the cheapest book"):
    if len(st.session_state.books) == 0:
        st.write("No books")
    else:
        # Поправка: Трябва да минем през всички книги с 'for'
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("The cheapest book is:")
        st.write(cheapest)
