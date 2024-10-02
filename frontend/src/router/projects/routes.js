export default [
    { path: '', component: () => import('../../views/projects/home.vue') },
    { path: ':uid', component: () => import('../../views/projects/details.vue') },
    { path: 'create', component: () => import('../../views/projects/create.vue') },
    { path: 'delete', component: () => import('../../views/projects/delete.vue') },
];