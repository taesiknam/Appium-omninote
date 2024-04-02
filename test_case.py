from omninote import Open_APP, Open_FAB, Open_Text_note, Write_Title, Write_Body, Click_back

def test_open_app_correctly_opens_home_page(Open_APP):
    # Test 실행
    assert Open_APP.text == "Notes", "Failed: 예상 결과와 실제 결과가 다릅니다."
    print("=====앱 실행 후 'Notes' 텍스트 확인 성공=====")

def test_open_FAB_displays_text_note_option(Open_FAB):
    assert Open_FAB.text == "Text note", "Failed: FAB 노출 실패"
    print("====FAB 선택 후 'Text note' 텍스트 확인 성공====")

def test_open_TestNote_display_Title(Open_Text_note):
  assert Open_Text_note.text == "Title", "Failed : Text Note 오픈 실패"
  print("====TextNote 진입 확인 성공====")

def test_open_TestNote_Title(Write_Title):
  print(type(Write_Title))
  assert Write_Title.text == "Hello World", "Failed : Text Note 오픈 실패"
  print("====Title 입력 확인====")

def test_open_TestNote_Body(Write_Body):
  print(type(Write_Body))
  assert Write_Body.text == "Hello World", "Failed : Text Note 오픈 실패"
  print("====Body 입력 확인====")


def test01_open_TestNote_Back(Click_back):
  assert Click_back == "Hello World", "Back 버튼 동작 안됨"
  print("====Back 버튼 동작 성공====")

def test02_open_TestNote_Back(Click_back):
  assert Click_back['result_title'] == "Hello World", "글 작성 실패"
  assert Click_back['result_body'] == "Hello World", "글 작성 실패"
  print("====글 작성 성공====")