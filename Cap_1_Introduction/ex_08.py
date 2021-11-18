# EXERCISE 8 : Widgets and Gizmos

WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

widgets = int(input('Enter the number of wigets: '))
gizomos = int(input('Enter the number of gizmos: '))
total_weight = (widgets * WIDGET_WEIGHT) + (gizomos + GIZMO_WEIGHT)

print('The total weight is %.2f g' % total_weight)
