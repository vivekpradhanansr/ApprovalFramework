from Reimburse.models import Reimburse, Transaction
from Reimburse.serializers import ReimburseSerializer, TransactionSerializer
from helpers import manager


PROCESS = {
    'reimburse_raise': {
        'name': 'Raising For Reimbursement',
        'model': Reimburse,
        'role': 'Submitter',
        'serializer': ReimburseSerializer,
        'transitions': ['manager_approval']
    },
    'manager_approval': {
        'name': 'Manager Approval',
        'model': Transaction,
        'role': 'Reviewer',
        'method': manager,
        'serializer': TransactionSerializer,
        'transitions': ['finance_approval']
    },
    'finance_approval': {
        'name': 'Finance Approval',
        'model': Transaction,
        'role': 'Reviewer',
        'method': manager,
        'serializer': TransactionSerializer,
        'transitions': None
    }
}

INITIAL = 'reimburse_raise'

TITLE = 'Reimbursement for ANSR Source'
DESCRIPTION = 'Reimbursement Process '
