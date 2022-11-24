from django import forms
from django.forms import ClearableFileInput
from django.template.loader import render_to_string

class CounterTextInput(forms.TextInput):
    template_name = "widgets/counters_text.html"
    
# 각 field에는 대응되는 widget이 존재한다.
# file, imagefield의 경우에는 기본적으로 Clearable File input이 사용됨.
# 커스텀 widget 이름: PreviewImageWidget
class PreviewImageWidget(forms.ClearableFileInput):
    # template_name = "widgets/preview_file.html"
    
    # class Media:
    #     js = [
    #         "http://code.jquery.com/jquery-3.6.1.min.js",
    #     ]
    def render(self, name, value, attrs=None, renderer=None):
        # 커스텀 위젯 템플릿으로 전달할 context를 만들어주고
        context = {
            'value': value,
            'name': name,
            'id': attrs['id']
        }

        # render_to_string을 이용해 HTML코드와 context를 잘 버무려줍니다.
        html = render_to_string(
            'widgets/preview_file.html', context)

        # 아래 코드를 통해 상속받은 위젯의 HTML코드를 불러울 수 있습니다.
        # parent_html = super().render(name, value, attrs, renderer)

        # 또 아래와 같이 .py 코드에서 스크립트를 짜서 동작토록 할수도 있습니다.
        # 이렇게 하려면 아래 return html + inline_code 이런식으로 하면 되겠죠?  
        # inline_code = mark_safe(
        #    <script>
        #        $('.btn').change(function() {
        #            alert('테스트');
        #        });
        #    </script>
        # )

        # 그리고 return 해주면 끝
        return html