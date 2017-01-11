from Reimburse.models import Reimburse, Transaction
from Reimburse.serializers import ReimburseSerializer, TransactionSerializer


PROCESS = {
    'reimburse_raise': {
        'name': 'Raising For Reimbursement',
        'model': Reimburse,
        'role': 'Submitter',
        'serializer': ReimburseSerializer,
        'transitions': {
            'manager_approval': 'manager'
        }
    },
    'manager_approval': {
        'name': 'Manager Approval',
        'model': Transaction,
        'role': 'Reviewer',
        'serializer': TransactionSerializer,
        'transitions': None
    }
}

INITIAL = 'reimburse_raise'

TITLE = 'Reimbursement for ANSR Source'
DESCRIPTION = 'Reimbursement Process '
