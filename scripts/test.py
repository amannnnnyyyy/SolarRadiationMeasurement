def testfunc(x,st):
    if(x):
        st.write(f'The name you entered is: {x}')


def removeText(st):
    is_clicked = st.button('Remove Text')
    if(is_clicked):
        testfunc('',st)