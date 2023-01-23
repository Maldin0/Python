'''PSCP Program'''
from json import loads as lds
# class LoremipsumdolorsitametconsecteturadipiscingelitNamnonsapiensitametenimrhoncusfeugiatvitaesedenimMorbipharetratempusultricesInvitaevulputatenisisedtincidunttellusSuspendissevitaesuscipitest(Exception):
#     '''Custom error test'''
#     def __init__(self, message="Testing <e>Judge. No error here, everything working as expected."):
#         self.message = message
#         super().__init__(self.message)

def main():
    '''8416-Reachability 05/11/2022'''
    node_connections, connected_node = lds(input().replace("'", '"')), [input()]
    for _ in range(4):
        for i, j in node_connections.items():
            if i in connected_node:
                connected_node.extend(j)
    print(sorted(set(connected_node)))
    # raise LoremipsumdolorsitametconsecteturadipiscingelitNamnonsapiensitametenimrhoncusfeugiatvitaesedenimMorbipharetratempusultricesInvitaevulputatenisisedtincidunttellusSuspendissevitaesuscipitest
main()
