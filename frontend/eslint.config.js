import js from '@eslint/js';

export default [
	{
		ignores: ['node_modules', 'dist', 'build', '.svelte-kit/', 'package/', '.env', '.env.*']
	},
	{
		files: ['**/*.js'],
		languageOptions: {
			ecmaVersion: 2021,
			sourceType: 'module',
			globals: {
				console: 'readonly',
				process: 'readonly'
			}
		},
		rules: {
			...js.configs.recommended.rules,
			'no-unused-vars': 'warn',
			'no-console': 'off'
		}
	}
];
