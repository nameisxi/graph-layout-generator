import unittest

from radial_layout import RadialLayout


class TestRadialLayout(unittest.TestCase):
    graph_1 = {}
    rl_1 = RadialLayout(graph_1, circumference=1)

    graph_2 = {
        'root': { 
            'id': 'root',
            'depth': 0,
            'parent': None,
            'children': [
                {'id': 'child_1','depth': 1,'parent': 'root',},
                {'id': 'child_2','depth': 1,'parent': 'root',},
                {'id': 'child_3','depth': 1,'parent': 'root',}
            ]
        },
        'child_1': { 
            'id': 'child_1',
            'depth': 1,
            'parent': 'root',
            'children': []
        },
        'child_2': { 
            'id': 'child_2',
            'depth': 1,
            'parent': 'root',
            'children': []
        },
        'child_3': { 
            'id': 'child_3',
            'depth': 1,
            'parent': 'root',
            'children': []
        }
    }
    rl_2 = RadialLayout(graph_2, circumference=1)

    graph_3 = {
        'root': { 
            'id': 'root',
            'depth': 0,
            'parent': None,
            'children': [
                {'id': 'child_1','depth': 1,'parent': 'root',},
                {'id': 'child_2','depth': 1,'parent': 'root',}
            ]
        },
        'child_1': { 
            'id': 'child_1',
            'depth': 1,
            'parent': 'root',
            'children': [
                {'id': 'child_1.1','depth': 2,'parent': 'child_1',},
                {'id': 'child_1.2','depth': 2,'parent': 'child_1',}
            ]
        },
        'child_2': { 
            'id': 'child_2',
            'depth': 1,
            'parent': 'root',
            'children': [
                {'id': 'child_2.1','depth': 2,'parent': 'child_2',},
                {'id': 'child_2.2','depth': 2,'parent': 'child_2',}
            ]
        },
        'child_1.1': { 
            'id': 'child_1.1',
            'depth': 2,
            'parent': 'child_1',
            'children': [
                {'id': 'child_1.1.1','depth': 3,'parent': 'child_1.1',},
                {'id': 'child_1.1.2','depth': 3,'parent': 'child_1.1',}
            ]
        },
        'child_1.2': { 
            'id': 'child_1.2',
            'depth': 2,
            'parent': 'child_1',
            'children': [
                {'id': 'child_1.2.1','depth': 3,'parent': 'child_1.2',}
            ]
        },
        'child_2.1': { 
            'id': 'child_2.1',
            'depth': 2,
            'parent': 'child_2',
            'children': [
                {'id': 'child_2.1.1','depth': 3,'parent': 'child_2.1',},
                {'id': 'child_2.1.2','depth': 3,'parent': 'child_2.1',},
                {'id': 'child_2.1.3','depth': 3,'parent': 'child_2.1',}
            ]
        },
        'child_2.2': { 
            'id': 'child_2.2',
            'depth': 2,
            'parent': 'child_2',
            'children': []
        },
        'child_1.1.1': { 
            'id': 'child_1.1.1',
            'depth': 3,
            'parent': 'child_1.1',
            'children': []
        },
        'child_1.1.2': { 
            'id': 'child_1.1.2',
            'depth': 3,
            'parent': 'child_1.1',
            'children': []
        },
        'child_1.2.1': { 
            'id': 'child_1.2.1',
            'depth': 3,
            'parent': 'child_1.2',
            'children': []
        },
        'child_2.1.1': { 
            'id': 'child_2.1.1',
            'depth': 3,
            'parent': 'child_2.1',
            'children': []
        },
        'child_2.1.2': { 
            'id': 'child_2.1.2',
            'depth': 3,
            'parent': 'child_2.1',
            'children': []
        },
        'child_2.1.3': { 
            'id': 'child_2.1.3',
            'depth': 3,
            'parent': 'child_2.1',
            'children': []
        },
    }
    rl_3 = RadialLayout(graph_3, circumference=1)

    def test_get_leaf_count(self):
        # Graph 1 - empty graph
        self.assertEqual(self.rl_1.get_leaf_count({}), 0)

        # Graph 2 - root node
        self.assertEqual(self.rl_2.get_leaf_count(
            {
                'id': 'root', 
                'depth': 0, 
                'parent': None, 
                'children': [
                    {'id': 'child_1', 'depth': 1, 'parent': 'root'}, 
                    {'id': 'child_2', 'depth': 1, 'parent': 'root'}, 
                    {'id': 'child_3', 'depth': 1, 'parent': 'root'}
                ], 
            }
        ), 3)
        # Graph 2 - node 1
        self.assertEqual(self.rl_2.get_leaf_count(
            { 
                'id': 'child_1',
                'depth': 1,
                'parent': 'root',
                'children': []
            }
        ), 1)
        # Graph 2 - node 3
        self.assertEqual(self.rl_2.get_leaf_count(
            { 
                'id': 'child_3',
                'depth': 1,
                'parent': 'root',
                'children': []
            }
        ), 1)
        
        # Graph 3 - root
        self.assertEqual(self.rl_3.get_leaf_count(
            {
                'id': 'root', 
                'depth': 0, 
                'parent': None, 
                'children': [
                    {
                        'id': 'child_1', 
                        'depth': 1, 
                        'parent': 'root'
                    }, 
                    {
                        'id': 'child_2', 
                        'depth': 1, 
                        'parent': 'root'
                    }
                ], 
            }
        ), 7)
        # Graph 3 - node 1
        self.assertEqual(self.rl_3.get_leaf_count(
            { 
                'id': 'child_1',
                'depth': 1,
                'parent': 'root',
                'children': [
                    {'id': 'child_1.1','depth': 2,'parent': 'child_1'},
                    {'id': 'child_1.2','depth': 2,'parent': 'child_1'}
                ]
            }
        ), 3)
        # Graph 2 - node 2.1
        self.assertEqual(self.rl_3.get_leaf_count(
            {
                'id': 'child_2.1', 
                'depth': 2, 
                'parent': 'child_2', 
                'children': [
                    {'id': 'child_2.1.1', 'depth': 3, 'parent': 'child_2.1'}, 
                    {'id': 'child_2.1.2', 'depth': 3, 'parent': 'child_2.1'}, 
                    {'id': 'child_2.1.3', 'depth': 3, 'parent': 'child_2.1'}
                ]
            }
        ), 3)

    def test_get_coordinates(self):
        # Graph 1
        self.assertEqual(self.rl_1.x_coordinates, [])
        self.assertEqual(self.rl_1.y_coordinates, [])

        # Graph 2
        self.assertEqual(
            self.rl_2.x_coordinates, 
            [0, 0.07957747154594769, -0.15915494309189535, 0.07957747154594756]
        )
        self.assertEqual(
            self.rl_2.y_coordinates, 
            [0, 0.13783222385544802, 1.9490859162596877e-17, -0.13783222385544808]
        )

        # Graph 3
        self.assertEqual(self.rl_3.x_coordinates, 
            [
                0,0.035415306580572625,
                0.7227212857919374,
                1.945331384703417,
                0.4804571744932015,
                -0.7227212857919372,
                -1.3462110876506705,
                -0.03541530658057265,
                -0.7227212857919375,
                -2.1591549430918953,
                -1.3462110876506712,
                0.48045717449320097,
                1.0443625168009978
            ]
        )
        self.assertEqual(self.rl_3.y_coordinates, 
            [
                0,
                0.15516459638199848,
                0.9062638275676811,
                0.93682222004287,
                2.1050204207456455,
                0.9062638275676813,
                1.6880953100357112,
                -0.15516459638199848,
                -0.9062638275676811,
                2.644202189920675e-16,
                -1.6880953100357108,
                -2.1050204207456455,
                -0.502938480925312
            ]
        )


if __name__ == '__main__':
    unittest.main()
