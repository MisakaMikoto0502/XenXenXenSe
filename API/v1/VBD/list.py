from fastapi import APIRouter
from XenGarden.session import create_session
from XenGarden.VBD import VBD

from API.v1.VBD.serialize import serialize
from config import get_xen_clusters

router = APIRouter()


@router.get("/{cluster_id}/vbd/list")
async def vbd_list(cluster_id: str):
    """ Get VBD by UUID """
    session = create_session(
        _id=cluster_id, get_xen_clusters=get_xen_clusters()
    )
    vbds = VBD.get_all(session)

    __vbd_list = []
    _vbd_list = __vbd_list.append
    for vbd in vbds:
        _vbd_list(serialize(vbd))

    if vbds is not None:
        ret = dict(success=True, data=__vbd_list)
    else:
        ret = dict(success=False)

    session.xenapi.session.logout()
    return ret
