types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def remove_duplicates(tickets):
    seen = []          # тикеты, которые уже встречались
    result = {}        

    for level, ticket_list in tickets.items():
        unique = []    # чистый список для текущего уровня
        for ticket in ticket_list:
            if ticket not in seen:
                unique.append(ticket)
                seen.append(ticket)
        result[level] = unique
    return result

def get_tickets_by_type(types, tickets):
    unique_tickets = remove_duplicates(tickets)  
    tickets_by_type = {}

    for level, name in types.items():
        tickets_by_type[name] = unique_tickets[level]

    return tickets_by_type


print(get_tickets_by_type(types, tickets))
