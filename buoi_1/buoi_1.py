#Nhap vao ho ten, nganh hoc, nam hoc, stt,
#Xuat ho ten theo tieng anh va mssv tuong ung
var = 1
while var == 1:
    ho_ten = input('Nhap ho ten: ')
    nganh_hoc = input('Nhap nganh hoc: ')
    nam_hoc = input('Nhap nam hoc: ')
    stt = input('Nhap stt: ')

    mssv_nganh = '0'
    if nganh_hoc == 'ktm':
        mssv_nganh = '119'
    elif nganh_hoc == 'vt':
        mssv_nganh = '141'
    elif nganh_hoc == 'dt':
        mssv_nganh = '151'
    elif nganh_hoc == 'ta':
        mssv_nganh = '153'
    elif nganh_hoc == 'ys':
        mssv_nganh = '155'
    elif nganh_hoc == 'iot':
        mssv_nganh = '160'

    mssv_nam = nam_hoc[2] + nam_hoc[3]
    if len(stt) == 1:
        mssv = mssv_nam + mssv_nganh + '00' + stt
    elif len(stt) == 2:
        mssv = mssv_nam + mssv_nganh + '0' + stt
    else:
        mssv = mssv_nam + mssv_nganh + stt
    
    mang_ho_ten = ho_ten.split(' ')
    name = mang_ho_ten[len(mang_ho_ten)-1] + ' ' + mang_ho_ten[0]
    print ('Ten tieng anh: ',name)
    print ('MSSV: ',mssv)
    print ('*************************************************')
