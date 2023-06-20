from django.core.exceptions import ValidationError
from datetime import datetime

def validate_timestamp(value):
    today = datetime.now().date()
    
    if value < today:
        raise ValidationError("Timestamp kecmis zamanda ola bilmez!!!")
    
    # Bu ders zamani muellimin izzah etdiyi validators
    
    
    
class CanceledWordsValidator:
    canceled_words = ['salam', 'necesen', 'python']  # Olmasini istemediyimiz sozler

    def __call__(self, value):
        for word in self.canceled_words:
            if word in value:
                raise ValidationError(
                    f"Qadagan olunmus bir soz >>{word} istifade edile bilmez!!!"
                )


def validate_content(value):   
    # Yuxaridaki yaratdigim validators class oldugu ucun onu modeldeki fieldimde gostere bilmeyecem ve migrate ederken xeta alacam buna gore onu basqa bir validatora menimsedib ele tanidiram :D
    validator = CanceledWordsValidator()
    validator(value)     