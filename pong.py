import pygame, sys, random


def ball_animation():
    # fixes local variables error
    # global variables can be used anywhere
    global ball_speed_x, ball_speed_y, score, bot_score
    # allows ball to move
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # allows ball to collide and bounce off the sides of the windows
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        bot_score += 1
        ball_restart()
    if ball.right >= SCREEN_WIDTH:
        score += 1
        ball_restart()

    # if the ball collides with player or bots rect
    if ball.colliderect(player) or ball.colliderect(bot):
        ball_speed_x *= -1


# makes player rectangles stay in the window
def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


# creates the 2nd player bot
def bot_ai():
    bot_speed = 7
    if bot.top < ball.y:
        bot.top += bot_speed
    if bot.bottom > ball.y:
        bot.bottom -= bot_speed
    if bot.top <= 0:
        bot.top = 0
    if bot.bottom >= SCREEN_HEIGHT:
        bot.bottom = SCREEN_HEIGHT


# puts ball back in center when goes beyond left or right side of window
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# pygame setup
pygame.init()
clock = pygame.time.Clock()

# creates screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# creates rectangle(x, y, length, width)
player = pygame.Rect((20, 250, 20, 80))
bot = pygame.Rect(760, 250, 20, 80)

# creates ball
ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# ball speed
ball_speed_x = 7
ball_speed_y = 7

# Creates scoreboard
score = 0
bot_score = 0
SCORE_FONT = pygame.font.SysFont("Courier", 50)

run = True
# while the game is running
while run:

    # updating window at 60fps
    pygame.display.flip()
    clock.tick(60)

    # updates screen after rectangle moves
    screen.fill(black)

    # Visuals
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, bot)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    # creates score text with render(f string, antialiasing, color)
    score_text = SCORE_FONT.render(f"{score}", True, white)
    bot_score_text = SCORE_FONT.render(f"{bot_score}", True, white)
    screen.blit(score_text, (SCREEN_WIDTH/4 - score_text.get_width()/2, 20))
    screen.blit(bot_score_text, (SCREEN_WIDTH * (3/4) - bot_score_text.get_width()/2, 20))

    ball_animation()
    player_animation()
    bot_ai()

    # player 1
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -7)
    elif key[pygame.K_s]:
        player.move_ip(0, 7)

    # ends the game after someone reaches 10 points
    if score >= 10:
        # creates "GAME OVER" text
        screen.fill(black)
        game_over_string = "GAME OVER"
        GAME_OVER_TEXT_FONT = pygame.font.SysFont("Courier", 70)
        game_over_text = GAME_OVER_TEXT_FONT.render(f"{game_over_string}", True, white)
        screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, 20))

        # creates the winner text
        win_string = "Player 1 wins!"
        win_text = GAME_OVER_TEXT_FONT.render(f"{win_string}", True, white)
        screen.blit(win_text, (SCREEN_WIDTH/2 - win_text.get_width()/2, 100))
    elif bot_score >= 10:
        # creates "GAME OVER" text
        screen.fill(black)
        game_over_string = "GAME OVER"
        GAME_OVER_TEXT_FONT = pygame.font.SysFont("Courier", 70)
        game_over_text = GAME_OVER_TEXT_FONT.render(f"{game_over_string}", True, white)
        screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, 20))

        # creates the winner text
        win_string = "Bot wins!"
        win_text = GAME_OVER_TEXT_FONT.render(f"{win_string}", True, white)
        screen.blit(win_text, (SCREEN_WIDTH / 2 - win_text.get_width()/2, 100))
    # for each event
    for event in pygame.event.get():
        # if x is clicked
        if event.type == pygame.QUIT:
            run = False
    # updates display so window stays open
    pygame.display.update()

pygame.quit()
sys.exit()
