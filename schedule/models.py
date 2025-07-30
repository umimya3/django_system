from django.db import models

class Event(models.Model):
    """
    イベント情報を格納するモデル
    """
    event_name = models.CharField("イベント名", max_length=200)
    memo = models.TextField("メモ", blank=True, null=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.event_name

class Candidate(models.Model):
    """
    イベントの候補日を格納するモデル
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="イベント")
    candidate_date = models.DateTimeField("候補日時")
    attendance = models.IntegerField("出欠", default=0)

    def __str__(self):
        return f"{self.event.event_name} - {self.candidate_date}"