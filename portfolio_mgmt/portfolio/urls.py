from rest_framework.routers import SimpleRouter
from .views import ProjectViewset, PortfolioViewset, UserProfileViewset

router = SimpleRouter()

router.register('portfolio', PortfolioViewset)
router.register('project', ProjectViewset)
router.register('profile', UserProfileViewset)


urlpatterns = router.urls