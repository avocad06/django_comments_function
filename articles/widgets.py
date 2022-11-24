from django import forms

class CounterTextInput(forms.TextInput):
    template_name = "widgets/counters_text.html"
    
# 각 field에는 대응되는 widget이 존재한다.
# file, imagefield의 경우에는 기본적으로 Clearable File input이 사용됨.
# 커스텀 widget 이름: PreviewImageWidget
class PreviewImageWidget(forms.ClearableFileInput):
    template_name = "widgets/preview_file.html"
    
    class Media:
        js = [
            "//code.jquery.com/jquery-3.6.1.min.js",
        ]