"""Views module stores all the views of the application"""

from shortner.new_view import NewView
from shortner.stub_view import StubView
from shortner.delete_view import DeleteView

from shortner.update_view import UpdateView
from shortner.login import login_test


__all__ = ["NewView", "StubView", "UpdateView", "DeleteView", "login_test"]
