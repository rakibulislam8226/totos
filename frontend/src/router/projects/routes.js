export default [
    { path: '', component: () => import('../../views/projects/list.vue') },
    { path: ':uid', component: () => import('../../views/projects/update.vue') },
    { path: 'create', component: () => import('../../views/projects/create.vue') },
    { path: 'delete', component: () => import('../../views/projects/delete.vue') },
];