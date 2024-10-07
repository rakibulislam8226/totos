export default [
    { path: 'login', component: () => import('../../views/authentications/login.vue') },
    { path: 'register', component: () => import('../../views/authentications/authentications.vue') },
];