//clang -o alert_payload.dylib alert_payload.m -framework Foundation -framework Cocoa -dynamiclib
#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>

__attribute__((constructor))
static void init(void){
    NSRunAlertPanel(@"Pwned.", @"Safari RCE by MWR Labs 2018 \\o/.", @"b00m", nil, nil);
}

