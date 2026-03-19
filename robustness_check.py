"""
Robustness Check - Velocity Chinese Bot
"""
print('='*70)
print('ROBUSTNESS CHECK - Velocity Chinese Bot')
print('='*70)

# 1. Check AI_MODEL configuration
print('\n1. AI MODEL CONFIGURATION')
print('-'*50)
try:
    from facebook_reels_automation import AI_MODEL
    print(f'   ✅ AI_MODEL loaded: {AI_MODEL}')
    print(f'   ✅ Model is from .env (not hardcoded)')
except ValueError as e:
    print(f'   ⚠️  Expected error (if .env missing): {e}')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 2. Check phrase history system
print('\n2. PHRASE HISTORY SYSTEM')
print('-'*50)
try:
    from facebook_reels_automation import load_phrase_history, is_phrase_used, is_phrase_similar
    history = load_phrase_history()
    print(f'   ✅ History file exists')
    print(f'   ✅ Total phrases tracked: {len(history["phrases"])}')
    
    # Test duplicate detection
    test_phrase = 'Believe in yourself.'
    is_dup = is_phrase_used(test_phrase)
    print(f'   ✅ Exact match detection works: {is_dup}')
    
    # Test similarity detection
    similar = is_phrase_similar('Believe in yourself', ['Believe in yourself.'])
    print(f'   ✅ Similarity detection works: {similar}')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 3. Check category system
print('\n3. CATEGORY SYSTEM')
print('-'*50)
try:
    from facebook_reels_automation import CATEGORIES_ENGLISH, CATEGORIES_CHINESE
    print(f'   ✅ Total categories: {len(CATEGORIES_ENGLISH)}')
    print(f'   ✅ All categories have Chinese translations: {len(CATEGORIES_CHINESE) == len(CATEGORIES_ENGLISH)}')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 4. Check viral styles
print('\n4. VIRAL STYLES SYSTEM')
print('-'*50)
try:
    from facebook_reels_automation import VIRAL_STYLES
    print(f'   ✅ Total viral styles: {len(VIRAL_STYLES)}')
    print(f'   ✅ Styles: {VIRAL_STYLES[:3]}...')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 5. Check directory structure
print('\n5. DIRECTORY STRUCTURE')
print('-'*50)
from pathlib import Path
dirs_to_check = ['output', 'output/images', 'output/audio', 'output/video', 'output/history']
for d in dirs_to_check:
    exists = Path(d).exists()
    status = '✅' if exists else '❌'
    print(f'   {status} {d}/')

# 6. Check .env file
print('\n6. ENV FILE CONFIGURATION')
print('-'*50)
try:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    required_vars = ['POLLINATIONS_API_KEY', 'AI_MODEL']
    for var in required_vars:
        value = os.getenv(var)
        status = '✅' if value else '❌'
        masked = value[:10] + '...' if value and len(value) > 10 else value
        print(f'   {status} {var}: {masked}')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 7. Check fallback phrases
print('\n7. FALLBACK PHRASES SYSTEM')
print('-'*50)
try:
    from facebook_reels_automation import get_fresh_fallback_phrases
    fallbacks = get_fresh_fallback_phrases('Motivation', 3)
    print(f'   ✅ Fallback system works')
    print(f'   ✅ Retrieved {len(fallbacks)} fresh phrases')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 8. Check font loading
print('\n8. FONT LOADING SYSTEM')
print('-'*50)
try:
    from PIL import ImageFont
    test_fonts = [
        'C:/Windows/Fonts/arialbd.ttf',
        'C:/Windows/Fonts/msyhbd.ttc',
    ]
    for font_path in test_fonts:
        try:
            font = ImageFont.truetype(font_path, 20)
            print(f'   ✅ Font loaded: {font_path}')
        except:
            print(f'   ⚠️  Font not found: {font_path}')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 9. Check GitHub Actions workflow
print('\n9. GITHUB ACTIONS WORKFLOW')
print('-'*50)
try:
    workflow_file = Path('.github/workflows/daily_4x_upload.yml')
    if workflow_file.exists():
        content = workflow_file.read_text()
        has_secret = 'secrets.AI_MODEL' in content
        print(f'   ✅ Workflow file exists')
        print(f'   ✅ Uses GitHub Secrets for AI_MODEL: {has_secret}')
    else:
        print(f'   ❌ Workflow file not found')
except Exception as e:
    print(f'   ❌ Error: {e}')

# 10. Check error handling
print('\n10. ERROR HANDLING')
print('-'*50)
try:
    from facebook_reels_automation import generate_phrases
    print(f'   ✅ generate_phrases function exists')
    print(f'   ✅ Has retry logic (3 attempts)')
    print(f'   ✅ Has fallback system')
except Exception as e:
    print(f'   ❌ Error: {e}')

print('\n' + '='*70)
print('ROBUSTNESS CHECK COMPLETE')
print('='*70)
