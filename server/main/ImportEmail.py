from gmail import Gmail
from rest_framework.views import APIView
from rest_framework.response import Response
from models import EmailSummary


class ImportEmail(APIView):
    """
    Fetch email from the server and store in DB
    """
    def get(self, request, limit=10):
        """
        Log in to gmail using credentials from our config file and retrieve
        email to store into our db
        """
        profile = request.user.get_profile()
        username = profile.gmail_username
        password = profile.gmail_password
        source = profile.gmail_source

        g = Gmail()
        g.login(username, password)
        msgs = g.inbox().mail(sender=source)

        imported = 0
        for msg in msgs[:int(limit)]:
            try:
                email_summary = EmailSummary.objects.get(
                    message_id=msg.message_id)
                continue
            except EmailSummary.DoesNotExist:
                pass
            msg.fetch()
            email_summary = EmailSummary.objects.create(
                user=request.user,
                message_id=msg.message_id,
                subject=msg.subject, date=msg.sent_at, source_addr=source,
                imported_to_wordpress=False
            )
            email_summary.save()
            imported += 1

        return Response({"response": "imported %s messages" % imported})
